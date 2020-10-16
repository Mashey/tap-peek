import requests
import json
from dotenv import load_dotenv
import os
from collections import defaultdict
import pandas as pd
import pprint
import singer
from datetime import datetime, timezone


with open('./tap_peek/activity_info_schema.json') as json_file:
    activity_info_schema = json.load(json_file)


pp = pprint.PrettyPrinter(indent=4, depth=3)

# args = singer.utils.parse_args(["token", "company_id"])
# company_id = args.config['company_id']
# API_KEY = args.config['token']

# The code below is for testing with Pytest.
load_dotenv()
API_KEY = json.loads(os.getenv("dandelion_chocolate"))['token']

headers = {
    'Authorization': API_KEY
}

client = requests.Session()


def fetch_transactions():
    payload = {
    }

    response = client.get(
        "https://pro-app.peek.com/services/reporting/api/reporting/transaction_records", headers=headers)
    transactions = parse_activities(response.json())

    # singer.write_schema('transactions', transactions_schema, 'id')
    # singer.write_records('transactions', transactions)

    return transactions


def fetch_core_activities():
    payload = {
        # "include": "activities%2Cactivities.resource_options",
        "legacy_id": "5bd78596c5cbe40069000007"
    }

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

    response = client.get(
        "https://pro-app.peek.com/services/once-pro/api/activities/partner/5bd78596c5cbe40069000007", headers=headers)
    core_addons = parse_activities(response.json())

    # singer.write_schema('core_addons', core_addons_schema, 'id')
    # singer.write_records('core_addons', core_addons)

    return core_addons


def fetch_timeslots():
    payload = {
    }

    response = client.get(
        "https://pro-app.peek.com/services/once-pro/api/timeslots", headers=headers)
    timeslots = parse_activities(response.json())

    # singer.write_schema('timeslots', timeslots_schema, 'id')
    # singer.write_records('timeslots', timeslots)

    return timeslots


transactions = fetch_transactions()
activities = fetch_core_activities()
addons = fetch_core_addons()
timeslots = fetch_timeslots()

test = 'variable'
