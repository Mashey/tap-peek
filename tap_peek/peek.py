import requests
import json
from dotenv import load_dotenv
import os
from collections import defaultdict
import pandas as pd
import pprint
import singer
from datetime import datetime, timezone


pp = pprint.PrettyPrinter(indent=4, depth=3)

# This code is for production.
args = singer.utils.parse_args(["token", "partner_id"])
API_KEY = args.config['token']
partner_id = args.config['partner_id']

# The code below is for testing with Pytest.
# load_dotenv()
# API_KEY = json.loads(os.getenv("dandelion_chocolate"))['token']
# partner_id = json.loads(os.getenv("dandelion_chocolate"))['partner_id']

headers = {
    'Authorization': API_KEY
}

client = requests.Session()


def fetch_transactions(new_start_date="2020-08-01", new_end_date="2020-08-25"):
    start_date = new_start_date
    end_date = new_end_date

    payload = {
        "fiql_query": f"partner_id=={partner_id};record_type=in=(purchase,reservation);purchase_type=in=(activity,addon,security_deposit,additional_charge);purchase_date=ge={start_date};purchase_date=le={end_date};currency==usd",
        "page_size": "50",
        "page": "use meta.next_page"
    }

    with open('./tap_peek/schemas/transactions_schema.json') as json_file:
        transactions_schema = json.load(json_file)

    response = client.get(
        "https://pro-app.peek.com/services/reporting/api/reporting/transaction_records", headers=headers, params=payload)

    transactions = response.json()

    singer.write_schema('transactions', transactions_schema, 'id')
    singer.write_records('transactions', transactions)

    return transactions


def fetch_core_activities():
    payload = {
        "include": "activities,activities.resource_options",
        "legacy_id": partner_id
    }

    with open('./tap_peek/schemas/activity_info_schema.json') as json_file:
        activity_info_schema = json.load(json_file)

    response = client.get(
        "https://pro-app.peek.com/services/pro/core/accounts", headers=headers, params=payload)

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
    with open('./tap_peek/schemas/core_addons_schema.json') as json_file:
        core_addons_schema = json.load(json_file)

    response = client.get(
        f"https://pro-app.peek.com/services/once-pro/api/activities/partner/{partner_id}", headers=headers)

    core_addons = response.json()

    singer.write_schema('core_addons', core_addons_schema, 'id')
    singer.write_records('core_addons', core_addons)

    return core_addons


def fetch_timeslots(start_date="2020-08-25", end_date="2020-10-15"):
    payload = {
        "start_date": start_date,
        "end_date": end_date
    }

    with open('./tap_peek/schemas/timeslots_schema.json') as json_file:
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
transactions = fetch_transactions()
