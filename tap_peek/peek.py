import requests
import json
from dotenv import load_dotenv
import os
from collections import defaultdict
import pandas as pd
import pprint
import singer
from datetime import datetime, timezone


# with open('./tap_peek/activity_info_schema.json') as json_file:
#     activity_info_schema = json.load(json_file)


# with open('./tap_peek/core_addons_schema.json') as json_file:
#     core_addons_schema = json.load(json_file)


# with open('./tap_peek/timeslots_schema.json') as json_file:
#     timeslots_schema = json.load(json_file)


pp = pprint.PrettyPrinter(indent=4, depth=3)

# args = singer.utils.parse_args(["token", "partner_id"])
# API_KEY = args.config['token']
# partner_id = args.config['partner_id']

# The code below is for testing with Pytest.
load_dotenv()
API_KEY = json.loads(os.getenv("dandelion_chocolate"))['token']
partner_id = json.loads(os.getenv("dandelion_chocolate"))['partner_id']

headers = {
    'Authorization': API_KEY
}

client = requests.Session()


def fetch_transactions():
    payload = {
    }

    response = client.get(
        "https://pro-app.peek.com/services/reporting/api/reporting/transaction_records", headers=headers)

    transactions = response.json()
    # singer.write_schema('transactions', transactions_schema, 'id')
    # singer.write_records('transactions', transactions)

    return transactions


def fetch_core_activities():
    payload = {
        # "include": "activities%2Cactivities.resource_options",
        "legacy_id": "5bd78596c5cbe40069000007"
    }

    with open('./tap_peek/activity_info_schema.json') as json_file:
        activity_info_schema = json.load(json_file)

    response = client.get(
        "https://pro-app.peek.com/services/pro/core/accounts?include=activities%2Cactivities.resource_options", headers=headers, params=payload)

    core_activities = parse_activities(response.json())

    singer.write_schema('activity_info', activity_info_schema, 'id')
    singer.write_records('activity_info', core_activities)

    return core_activities


def parse_activities(response):
    core_activities = []
    for activity in response["included"]:
        if activity["type"] == "core/activity":
            core_activities.append(activity)
        else:
            continue

    return core_activities


def fetch_core_addons():
    payload = {
    }

    with open('./tap_peek/core_addons_schema.json') as json_file:
        core_addons_schema = json.load(json_file)

    response = client.get(
        f"https://pro-app.peek.com/services/once-pro/api/activities/partner/{partner_id}", headers=headers)

    core_addons = response.json()

    singer.write_schema('core_addons', core_addons_schema, 'id')
    singer.write_records('core_addons', core_addons)

    return core_addons


def fetch_timeslots():
    payload = {
        "start_date": "2020-08-25",
        "end_date": "2020-10-15"
    }

    with open('./tap_peek/timeslots_schema.json') as json_file:
        timeslots_schema = json.load(json_file)

    response = client.get(
        "https://pro-app.peek.com/services/once-pro/api/timeslots", headers=headers, params=payload)

    timeslots = response.json()

    singer.write_schema('timeslots', timeslots_schema, 'fid')
    singer.write_records('timeslots', timeslots)

    return timeslots


activities = fetch_core_activities()
addons = fetch_core_addons()
timeslots = fetch_timeslots()
# transactions = fetch_transactions()

test = 'variable'
