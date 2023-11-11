from fastapi import APIRouter
from app.api.v1.routes import data

router = APIRouter()
router.include_router(data.router, tags=["data"])
