import requests

class PostcodesService:

    def __init__(self):
        self.api_url = 'http://api.postcodes.io/'

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
        response = requests.post('%spostcodes' % self.api_url, data={'geolocations': geolocations})
        print(response.json())