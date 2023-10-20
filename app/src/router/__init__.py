from fastapi import APIRouter

from .member import member_router

router = APIRouter(prefix="/api/v1")
router.include_router(member_router, tags=["member"])
