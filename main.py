import uvicorn
from fastapi import FastAPI
from infraestructure.controllers import processor_files_controller
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Process Service',
              description='This service use some flat file with csv format to process and search nearest '
                          'postcodes for a given longitude & latitude in postcodes.io API (https://postcodes.io/)',
              version='0.0.1')

origins = [
    "http://postalcodes_web_1:8000",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(processor_files_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)