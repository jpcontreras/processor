import csv
import shutil
import os
import json
from infraestructure.services.postcodes_service import PostcodesService
from infraestructure.lib.utils import Utils

class ProcessCsv:
    # Bulk translates geolocations into Postcodes. Accepts up to 100 geolocations.
    ROW_TO_REQUEST = 100

    # ===== Parameters:
    # *+file+:UploadFile
    def __init__(self, file):
        self.file = file
        self.total_rows = 0
        self.postal_codes_pack = []

    def run(self):
        with open(self.file.filename, "wb") as buffer:
            shutil.copyfileobj(self.file.file, buffer)
        file_path = f'./{self.file.filename}'
        name, extension = os.path.splitext(file_path)
        if extension == '.csv':
            self._file_access(file_path)
        else:
            raise Exception('Invalid file format. Expected .csv')
        os.remove(file_path)


    # ===== Parameters:
    # *+file_path+:String
    # ===== Return:
    # +Array<Json>+
    def _file_access(self, file_path):
        self.total_rows = sum(1 for row in (open(file_path)))
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            row_to_request = 1
            current_row = 1
            geolocations = []
            service = PostcodesService()
            for row in csv_reader:
                if current_row >= 2:
                    latitude = float(row[0])
                    longitude = float(row[1])
                    if Utils.is_valid_coordinates(latitude, longitude):
                        geolocations.append({
                            "longitude": longitude,
                            "latitude": latitude,
                            "radius": 1000,
                            "limit": 1
                        })
                        # TODO: search and learn about multiprocessing (https://rico-schmidt.name/pymotw-3/multiprocessing/basics.html)
                        if row_to_request == self.ROW_TO_REQUEST or current_row == self.total_rows:
                            response = service.bulk_search_nearest(geolocations)
                            data_string = json.loads(response)
                            if len(geolocations) != len(data_string['result']):
                                raise Exception('Some Geolocation of csv dont have Postal Code')
                            self.postal_codes_pack.append(data_string['result'])
                            geolocations = []
                            row_to_request = 0
                        row_to_request += 1
                    else:
                        ''
                        # TODO: should save in some variable total invalid coordinates to return the client
                current_row += 1
        return self.postal_codes_pack

