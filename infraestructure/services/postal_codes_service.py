import requests
import json

class PostalCodesService:
    API_URL = "http://postalcodes_web_1:8000/postal_codes"

    # ===== Parameters:
    # *+postal_code+: Json
    # ===== Description
    # Json format
    # {
    #   "latitude": 0,
    #   "longitude": 0,
    #   "postal_details": {}
    # }
    def create(self, postal_code):
        payload = postal_code
        headers = {'content-type': 'application/json'}
        return requests.post(f"{self.API_URL}/create", data=json.dumps(payload), headers=headers).text