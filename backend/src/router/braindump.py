from fastapi import APIRouter
from sqlmodel import Session
from src.models import Item
from src.schemas import BrainDumpResponse, BrainDumpRequest
from src.services import parse_text_to_item

router = APIRouter(prefix="/api/braindump", tags=["braindump"])

@router.post("/parse", response_model=BrainDumpResponse)
async def parse_braindump(payload: BrainDumpRequest):
    return parse_text_to_item(payload.raw_text)

