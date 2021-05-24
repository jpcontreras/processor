import csv
import shutil
import os
from infraestructure.services.postcodes_service import PostcodesService

class ProcessCsv:
    # ===== Parameters:
    # *+file+:UploadFile
    def __init__(self, file):
        self.file = file
        self.total_rows = 1
        self.geolocations = []

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
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # csv_total_rows = len(list(csv_reader))
            # print(f'csv_total_rows ===> {csv_total_rows}')

            rows_to_request = 0
            # service = PostcodesService
            for row in csv_reader:
                print(f'lat: {row[0]} lng: {row[1]}')
                if self.total_rows >= 2:
                    # print(f'rows_to_request ===> {rows_to_request}')
                    # print(f'total_rows ===> {self.total_rows}')
                    if rows_to_request == 100: #or self.total_rows == csv_total_rows:
                        #response = service.bulk_search_nearest(self.geolocations)
                        print(f'geolocations ===> {self.geolocations}')
                        self.geolocations = []
                        rows_to_request = 0
                    else:
                        print(f'lat: {row[0]} lng: {row[1]}')
                        self.geolocations.append({
                            "longitude": row[1],
                            "latitude": row[0],
                            "radius": 1000,
                            "limit": 1
                        })
                        rows_to_request += 1
                self.total_rows += 1
