import json
import requests

class PeekClient:
    BASE_URL = "https://pro-app.peek.com/services"

    def __init__(self, api_key):
        self._client = requests.Session()
        self._client.headers.update({'Authorization': api_key})

    def fetch_transactions(self, partner_id, start_date="2020-08-01", end_date="2020-08-25"):
        url    = f"{self.BASE_URL}/reporting/api/reporting/transaction_records"
        params = {
            "fiql_query": f"partner_id=={partner_id};record_type=in=(purchase,reservation);purchase_type=in=(activity,addon,security_deposit,additional_charge);purchase_date=ge={start_date};purchase_date=le={end_date};currency==usd",
            "page_size": "50",
            "page": "use meta.next_page"
        }
        return self._client.get(url, params=params).json()

    def fetch_core_activities(self, partner_id):
        url    = f"{self.BASE_URL}/pro/core/accounts"
        params = {
            "include": "activities,activities.resource_options",
            "legacy_id": partner_id
        }
        return self._client.get(url, params=params).json()

    def fetch_core_addons(self, partner_id):
        url = f"{self.BASE_URL}/once-pro/api/activities/partner/{partner_id}"
        return self._client.get(url).json()

    def fetch_timeslots(self, start_date="2020-08-25", end_date="2020-10-15"):
        url    = f"{self.BASE_URL}/once-pro/api/timeslots"
        params = {
            "start_date": start_date,
            "end_date": end_date
        }
        return self._client.get(url, params=params).json()
