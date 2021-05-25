import json
from infraestructure.services.postal_codes_service import PostalCodesService

class SendPostalCodes:

    # ===== Parameters:
    # *+postal_codes+:Array<Json>
    # ===== Description
    # Json format
    # {
    #     "query": {
    #         "longitude": "-2.49690382054704",
    #         "latitude": "53.5351312861402",
    #         "radius": "1000",
    #         "limit": "1"
    #     },
    #     "result": [
    #         {
    #             "postcode": "M46 9WU",
    #             "quality": 1,
    #             "eastings": 367163,
    #             "northings": 404390,
    #             "country": "England",
    #             "nhs_ha": "North West",
    #             "longitude": -2.496903,
    #             "latitude": 53.535127,
    #             "european_electoral_region": "North West",
    #             "primary_care_trust": "Ashton, Leigh and Wigan",
    #             "region": "North West",
    #             "lsoa": "Wigan 017C",
    #             "msoa": "Wigan 017",
    #             "incode": "9WU",
    #             "outcode": "M46",
    #             "parliamentary_constituency": "Bolton West",
    #             "admin_district": "Wigan",
    #             "parish": "Wigan, unparished area",
    #             "admin_county": null,
    #             "admin_ward": "Atherton",
    #             "ced": null,
    #             "ccg": "NHS Wigan Borough",
    #             "nuts": "Greater Manchester North West",
    #             "codes": {
    #                 "admin_district": "E08000010",
    #                 "admin_county": "E99999999",
    #                 "admin_ward": "E05000845",
    #                 "parish": "E43000164",
    #                 "parliamentary_constituency": "E14000580",
    #                 "ccg": "E38000205",
    #                 "ccg_id": "02H",
    #                 "ced": "E99999999",
    #                 "nuts": "UKD36",
    #                 "lsoa": "E01006241",
    #                 "msoa": "E02001303",
    #                 "lau2": "E05000845"
    #             },
    #             "distance": 0.4801241
    #         }
    #     ]
    # }
    def __init__(self, postal_codes):
        self.postal_codes = postal_codes

    def run(self):
        service = PostalCodesService()
        for data in self.postal_codes:
            for postal_code in data:
                payload = {
                  "latitude": postal_code['query']['latitude'],
                  "longitude": postal_code['query']['longitude'],
                  "postal_details": postal_code['result']
                }
                response = service.create(payload)
                data_string = json.loads(response)