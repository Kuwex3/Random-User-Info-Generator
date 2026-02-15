from fastapi import APIRouter
from backend.middlewares.get_random_info import get_info_by_api

router = APIRouter()

@router.get("/api/get/info")
async def send_info():
    return get_info_by_api()