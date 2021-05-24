import csv
import inspect
import shutil
import os

class ProcessCsv:
    # ===== Parameters:
    # *+file+:UploadFile
    def __init__(self, file):
        self.file = file

    def run(self):
        with open(self.file.filename, "wb") as buffer:
            shutil.copyfileobj(self.file.file, buffer)

        file_path = f'./{self.file.filename}'

        name, extension = os.path.splitext(file_path)
        if extension == '.csv':
            with open(file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                self.total_rows = 0
                for row in csv_reader:
                    if self.total_rows == 0:
                        print(f'Column names are {", ".join(row)}')
                        self.total_rows += 1
                    else:
                        print(f'lat: {row[0]} lng: {row[1]}')
                        self.total_rows += 1
                os.remove(file_path)
        else:
            raise RuntimeError('Invalid file format. Expected .csv')