import csv
import shutil
import os
from infraestructure.services.postcodes_service import PostcodesService
import json

class ProcessCsv:
    # Bulk translates geolocations into Postcodes. Accepts up to 100 geolocations.
    ROW_TO_REQUEST = 100

    # ===== Parameters:
    # *+file+:UploadFile
    def __init__(self, file):
        self.file = file
        self.total_rows = 0

    def run(self):
        with open(self.file.filename, "wb") as buffer:
            shutil.copyfileobj(self.file.file, buffer)
        file_path = f'./{self.file.filename}'
        name, extension = os.path.splitext(file_path)
        if extension == '.csv':
            self._file_access(file_path)
            # with open(file_path) as csv_file:
            #     csv_reader = csv.reader(csv_file, delimiter=',')
            #     self.total_rows = 0
            #     for row in csv_reader:
            #         if self.total_rows == 0:
            #             print(f'Column names are {", ".join(row)}')
            #             self.total_rows += 1
            #         else:
            #             print(f'lat: {row[0]} lng: {row[1]}')
            #             self.total_rows += 1
            #     os.remove(file_path)
        else:
            raise Exception('Invalid file format. Expected .csv')
        os.remove(file_path)


    # ===== Parameters:
    # *+file_path+:String
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
                    geolocations.append({
                        "longitude": float(row[1]),
                        "latitude": float(row[0]),
                        "radius": 1000,
                        "limit": 1
                    })
                    # TODO: search and learn about multiprocessing (https://rico-schmidt.name/pymotw-3/multiprocessing/basics.html)
                    if row_to_request == self.ROW_TO_REQUEST or current_row == self.total_rows:
                        print(f'Geolocations to send ===> {len(geolocations)}')
                        response = service.bulk_search_nearest(geolocations)
                        data_string = json.loads(response)
                        print('result:', len(data_string['result']))
                        # print('JSON:', data_string)

                        geolocations = []
                        row_to_request = 0

                    row_to_request += 1

                current_row += 1
