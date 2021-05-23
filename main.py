import uvicorn
from fastapi import FastAPI

app = FastAPI(title='Process Service',
              description='This service use some flat file with csv format to process and search nearest '
                          'postcodes for a given longitude & latitude in postcodes.io API (https://postcodes.io/)',
              version='0.0.1')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)