from typing import Annotated
from fastapi import APIRouter, Depends

from services.chat import PandasMetricsSerivce
from services.file_handler import FileHandler, S3Handler

router = APIRouter(
    prefix="/metrics",
    tags=["metrics", "pandas"],
    responses={404: {"description": "Not found"}}
)


def get_file_handler():
    return S3Handler()

@router.get("/{chat_id}")
def metrics(chat_id: str, file_handler: Annotated[FileHandler, Depends(get_file_handler)]):
    chat_df = file_handler.read_file(chat_id)
    chat_metrics = PandasMetricsSerivce(chat_df)
    response_metrics = chat_metrics.get_chat_metrics()
    print(f"{response_metrics= }")
    return {"metrics": response_metrics}

