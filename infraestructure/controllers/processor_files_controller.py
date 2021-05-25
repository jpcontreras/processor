from fastapi import APIRouter, File, UploadFile
from application.process_scv import ProcessCsv
from application.send_postal_codes import SendPostalCodes

router = APIRouter()

@router.post('/processor_files/create')
async def upload(file: UploadFile = File(...)):
    # try:
    process_interactor = ProcessCsv(file)
    process_interactor.run()
    # TODO: search an learn about triggers
    send_interactor = SendPostalCodes(process_interactor.postal_codes_pack)
    send_interactor.run()
    return { "total_process": process_interactor.total_rows }
    # except Exception as exc:
    #     return { "Error": exc }