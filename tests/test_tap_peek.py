import vcr
import pytest
import pytest_vcr
from tap_peek.peek import *


@pytest.mark.vcr()
def test_fetch_core_activities():
    api_response = fetch_core_activities()

    first_response = api_response[0]

    assert "id" in first_response
    assert "name" in first_response["attributes"]
    assert "legacy-id" in first_response["attributes"]
    assert "info-to-know" in first_response["attributes"]
    assert "info-to-bring" in first_response["attributes"]
    assert "info-meeting-location" in first_response["attributes"]
    assert "info-included" in first_response["attributes"]
    assert "image-url" in first_response["attributes"]
    assert "description" in first_response["attributes"]


@pytest.mark.vcr()
def test_fetch_core_addons():
    api_response = fetch_core_addons()

    first_response = api_response["activities"][0]

    assert "id" in first_response
    assert "created_at" in first_response
    assert "name" in first_response
    assert "status" in first_response
    assert "schedulable" in first_response
    assert "currency" in first_response
    assert "consumer_activity_status" in first_response
    assert "minimum_booking_count" in first_response
    assert "minimum_booking_prevents_purchase" in first_response
    assert "partner_id" in first_response

    if len(first_response["tickets"]) > 0:
        assert "id" in first_response["tickets"][0]
        assert "name" in first_response["tickets"][0]
        assert "description" in first_response["tickets"][0]
        assert "price" in first_response["tickets"][0]
        assert "price_after_tax" in first_response["tickets"][0]
        assert "status" in first_response["tickets"][0]
    else:
        assert len(first_response["tickets"]) == 0


@pytest.mark.vcr()
def test_fetch_timeslots():
    api_response = fetch_timeslots()

    first_response = api_response["timeslots"][0]

    assert "fid" in first_response
    assert "time_series_id" in first_response
    assert "activity_id" in first_response
    assert "start" in first_response
    assert "end" in first_response
    assert "date" in first_response
    assert "minute_length" in first_response
    assert "resources_names" in first_response
    assert "availability_status" in first_response
    assert "availability_max_party_size" in first_response
    assert "availability_total_capacity" in first_response
    assert "availability_available_spots" in first_response
    assert "availability_spots_taken" in first_response
    assert "private_availability_code" in first_response
    assert "time_series_type" in first_response
    assert "is_freesale" in first_response
    assert "is_fake" in first_response
    assert "checked_in_count" in first_response
    assert "manifest_notes" in first_response
