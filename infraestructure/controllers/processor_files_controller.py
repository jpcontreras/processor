from fastapi import APIRouter, File, UploadFile
from application.process_scv import ProcessCsv

router = APIRouter()

@router.post('/processor_files/create')
async def upload(file: UploadFile = File(...)):
    # try:
    interactor = ProcessCsv(file)
    interactor.run()
    return { "line_count": interactor.total_rows }
    # except Exception as exc:
    #     return { "Error": exc }