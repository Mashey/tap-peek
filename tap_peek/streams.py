import urllib.parse as urlparse
from urllib.parse import parse_qs

import singer

LOGGER = singer.get_logger()

def parse_activities(response):
    core_activities = []
    included = response.get('included', [])
    for activity in included:
        activity_type = activity.get('type', None)
        if activity_type == "core/activity":
            core_activities.append(activity)
    return core_activities

class Stream:
    tap_stream_id          = None
    key_properties         = []
    replication_method     = ''
    valid_replication_keys = []
    replication_key        = None
    object_type            = ''

    def __init__(self, client, state):
        self.client = client
        self.state = state

    def sync(self, *args, **kwargs):
        raise NotImplementedError("Sync of child class not implemented")

class CatalogStream(Stream):
    replication_method = 'INCREMENTAL'

class FullTableStream(Stream):
    replication_method = 'FULL_TABLE'

class ActivityInfo(FullTableStream):
    tap_stream_id  = 'activity_info'
    key_properties = ['id']
    object_type    = 'ACTIVITY_INFO'

    def sync(self, partner_id=None, *args, **kwargs):
        response = self.client.fetch_core_activities(partner_id)
        activities = parse_activities(response)
        for activity in activities:
            yield activity

class CoreAddons(FullTableStream):
    tap_stream_id  = 'core_addons'
    key_properties = ['id']
    object_type    = 'CORE_ADDON'

    def sync(self, partner_id=None, *args, **kwargs):
        response = self.client.fetch_core_addons(partner_id)
        core_addons = response.get('activities', [])
        for core_addon in core_addons:
            yield core_addon

class Transactions(CatalogStream):
    tap_stream_id  = 'transactions'
    key_properties = ['id']
    object_type    = 'TRANSACTION'

    def sync(self, partner_id=None, start_date=None, end_date=None, *args, **kwargs):
        current_page = 1
        total_pages = 1
        while current_page <= total_pages:
            response = self.client.fetch_transactions(partner_id, start_date, end_date, current_page)
            transactions = response.get('transactions', [])
            meta = response.get('meta', {})
            total_pages = meta.get('total_pages', 0)
            for transaction in transactions:
                yield transaction
            current_page = current_page + 1
        singer.write_bookmark(self.state, self.tap_stream_id, 'start_date', end_date)
        singer.write_state(self.state)

class Timeslots(CatalogStream):
    tap_stream_id  = 'timeslots'
    key_properties = ['fid']
    object_type    = 'TIMESLOT'

    def sync(self, partner_id=None, start_date=None, end_date=None, *args, **kwargs):
        response = self.client.fetch_timeslots(start_date, end_date)
        timeslots = response.get('timeslots', [])
        for timeslot in timeslots:
            yield timeslot
        singer.write_bookmark(self.state, self.tap_stream_id, 'start_date', end_date)
        singer.write_state(self.state)

STREAMS = {
    'activity_info': ActivityInfo,
    'core_addons': CoreAddons,
    'transactions': Transactions,
    'timeslots': Timeslots
}