from logging import getLogger

from fastapi import APIRouter


log = getLogger(__name__)
img_router = APIRouter(prefix="/image")
