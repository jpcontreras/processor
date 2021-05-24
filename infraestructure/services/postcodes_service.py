import requests
import json

class PostcodesService:
    API_URL = "https://api.postcodes.io/postcodes/"

    # ===== Parameters:
    # *+geolocations+: Array<Json>
    # ===== Description
    # Json format
    # {
    #   "longitude":  0.629834723775309,
    #   "latitude": 51.7923246977375,
    #   "radius": 1000,
    #   "limit": 1
    # }
    def bulk_search_nearest(self, geolocations):
        payload = {"geolocations": geolocations}
        headers = {'content-type': 'application/json'}
        return requests.post(self.API_URL, data=json.dumps(payload), headers=headers).text