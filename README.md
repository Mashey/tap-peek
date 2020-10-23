# tap-peek

**This tap is in development.**

This is a [Singer](https://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

## Description
This tap:
* Downloads data from [Peek](https://www.peek.com/pro/)
* Extracts from the following sources to produce [streams](https://github.com/Mashey/tap-peek/blob/master/tap_peek/streams.py). Below is a list of all the streams available. See the [streams file](https://github.com/Mashey/tap-peek/blob/master/tap_peek/streams.py) for a list of classes where each one has a constant indiciating if the stream's replication_method is INCREMENTAL or FULL_TABLE.
    * ActivityInfo
    * CoreAddons
    * Timeslots
    * Transactions

* Includes a schema for each resource reflecting most recent tested data retrieved using the api. See [the schema folder](https://github.com/Mashey/tap-peek/blob/master/tap_peek/schemas) for details.

## Authentication

Authentication is handled with a valid Peek Pro account. In the tap configuration the following fields are required for authentication to work correctly:

* token
* partner_id

## Quick Start

1. Install

    Clone this repository, and then install using setup.py. We recommend using a virtualenv:

    ```bash
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ pip install -e .
    ```
1. Create your tap's `config.json` file.  The tap config file for this tap should include these entries:
   - `start_date` - the default value to use if no bookmark exists for an endpoint (rfc3339 date string)

   And the other values mentioned in [the authentication section above](#authentication).

    ```json
	{
		"token": "Bearer <api_token>",
		"partner_id": "<partner_id>",
		"start_date": "2020-08-21T00:00:00Z"
	}
	```

1. Run the Tap in Discovery Mode
    This creates a catalog.json for selecting objects/fields to integrate:
    ```bash
    tap-peek --config config.json --discover > catalog.json
    ```
   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode).

5. Run the Tap in Sync Mode (with catalog) and [write out to state file](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#running-a-singer-tap-with-a-singer-target)

    For Sync mode:
    ```bash
    $ tap-peek --config tap_config.json --catalog catalog.json >> state.json
    $ tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```
    To load to json files to verify outputs:
    ```bash
    $ tap-peek --config tap_config.json --catalog catalog.json | target-json >> state.json
    $ tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```
---