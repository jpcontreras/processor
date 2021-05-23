from fastapi import FastAPI

app = FastAPI(title='Postal Codes Service',
              description='This service use some flat file with csv format to save and send to another service to process data.',
              version='0.0.1')
