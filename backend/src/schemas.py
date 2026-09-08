from pydantic import BaseModel
from typing import List

class BrainDumpRequest(BaseModel):
    raw_text: str

class ParsedItem(BaseModel):
    title: str
    description: str
    category: str

class BrainDumpResponse(BaseModel):
    tickets: List[ParsedItem]