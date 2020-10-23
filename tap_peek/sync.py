import singer
from singer import Transformer, metadata
from .client import PeekClient
from .streams import STREAMS


LOGGER = singer.get_logger()

def sync(config, state, catalog):
    client = PeekClient(config['token'])
    partner_id = config['partner_id']

    with Transformer() as transformer:
        for stream in catalog.get_selected_streams(state):
            tap_stream_id   = stream.tap_stream_id
            stream_obj      = STREAMS[tap_stream_id](client, state)
            replication_key = stream_obj.replication_key
            stream_schema   = stream.schema.to_dict()
            stream_metadata = metadata.to_map(stream.metadata)

            LOGGER.info('Staring sync for stream: %s', tap_stream_id)

            state = singer.set_currently_syncing(state, tap_stream_id)
            singer.write_state(state)

            singer.write_schema(
                tap_stream_id,
                stream_schema,
                stream_obj.key_properties,
                stream.replication_key
            )

            start_date = singer.get_bookmark(state, tap_stream_id, replication_key, config['start_date'])
            end_date = singer.utils.strftime(singer.utils.now(), format_str=singer.utils.DATETIME_PARSE)

            for record in stream_obj.sync(partner_id=partner_id, start_date=start_date, end_date=end_date):
                LOGGER.info(f"Writing record: {record}")
                transformed_record = transformer.transform(record, stream_schema, stream_metadata)
                singer.write_record(
                    tap_stream_id,
                    transformed_record,
                )
            state = singer.clear_bookmark(state, tap_stream_id, 'start_date')
            singer.write_state(state)

    state = singer.set_currently_syncing(state, None)
    singer.write_state(state)