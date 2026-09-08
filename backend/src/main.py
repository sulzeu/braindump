from fastapi import FastAPI
from dotenv import load_dotenv

from src.router import braindump

# To run the backend
# uvicorn src.main:app --reload
app = FastAPI(
    title="Braindump API",
    version="1.0.0"
)

app.include_router(braindump.router)

@app.get("/")
async def root():
    return { "message": "Braindump API is running" }