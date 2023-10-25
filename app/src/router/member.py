# --------------------------------------------------------------------------
# Member model의 API router을 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from logging import getLogger
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from src.db import database
from src.schemas import member as schemas
from src.crud import member as crud

log = getLogger(__name__)
member_router = APIRouter(prefix="/member")


@member_router.post(
    "/",
    response_model=schemas.Member,
    summary="Create a new member",
    description="Create a new member with the given name and email",
)
async def create_new_member(
    member: schemas.MemberCreate, db: AsyncSession = Depends(database.get_db)
):
    return await crud.create_member(db, member)


@member_router.get(
    "/{member_id}",
    response_model=schemas.Member,
    summary="Read a member",
    description="Read a member with the given id",
)
async def read_member(member_id: int, db: AsyncSession = Depends(database.get_db)):
    db_member = await crud.get_member(db, member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member


@member_router.get(
    "/email/{email}",
    response_model=schemas.Member,
    summary="Read a member by email",
    description="Read a member with the given email",
)
async def read_member_by_email(email: str, db: AsyncSession = Depends(database.get_db)):
    db_member = await crud.get_member_by_email(db, email)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member


@member_router.get(
    "/",
    response_model=List[schemas.Member],
    summary="Read members",
    description="Read members with the given skip and limit",
)
async def read_members(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(database.get_db)
):
    log.info(f"Reading members with skip: {skip} and limit: {limit}")
    return await crud.get_members(db, skip=skip, limit=limit)


@member_router.put(
    "/{member_id}",
    response_model=schemas.Member,
    summary="Update a member",
    description="Update a member with the given id",
)
async def update_existing_member(
    member_id: int,
    member: schemas.MemberUpdate,
    db: AsyncSession = Depends(database.get_db),
):
    updated_member = await crud.update_member(db, member_id, member)
    if updated_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated_member


@member_router.delete(
    "/{member_id}",
    response_model=int,
    summary="Delete a member",
    description="Delete a member with the given id",
)
async def delete_existing_member(
    member_id: int, db: AsyncSession = Depends(database.get_db)
):
    deleted_member_id = await crud.delete_member(db, member_id)
    if deleted_member_id is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return deleted_member_id
