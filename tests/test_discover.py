import json
import vcr
import pytest
import pytest_asyncio
from tap_peek.client import PeekClient
from tap_peek.discover import *

import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
company_id = os.getenv("COMPANY_ID")

@pytest.mark.asyncio
async def test_get_schemas():
    with open("tap_peek/schemas/activity_info.json") as file:
        activity_info_schema = json.load(file)
    with open("tap_peek/schemas/core_addons.json") as file:
        core_addons_schema = json.load(file)
    with open("tap_peek/schemas/timeslots.json") as file:
        timeslots_schema = json.load(file)
    with open("tap_peek/schemas/transactions.json") as file:
        transactions_schema = json.load(file)

    expected_schemas = {
        'activity_info': activity_info_schema,
        'core_addons': core_addons_schema,
        'timeslots': timeslots_schema,
        'transactions': transactions_schema
    }

    schemas, schemas_metadata = get_schemas()

    assert schemas == expected_schemas

@pytest.mark.asyncio
async def test_discover():
    catalog = discover()

    assert len(catalog.streams) == 4