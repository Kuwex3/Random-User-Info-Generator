from fastapi import FastAPI
from backend.get_info import router as get_info_router

app = FastAPI()

app.include_router(router=get_info_router)

@app.get("/")
async def main_page():
    return "Hello, World!"