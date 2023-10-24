# --------------------------------------------------------------------------
# Member model의 API router을 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from logging import getLogger
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from src.db import database
from src.schemas import member as schemas
from src.crud.member import (
    create_member,
    get_member,
    get_member_by_email,
    get_members,
    update_member,
    delete_member,
)

log = getLogger(__name__)
member_router = APIRouter(prefix="/member")


@member_router.post(
    "/",
    response_model=schemas.Member,
    summary="Create a new member",
    description="Create a new member with the given name and email",
)
def create_new_member(
    member: schemas.MemberCreate, db: Session = Depends(database.get_db)
):
    return create_member(db, member)


@member_router.get(
    "/{member_id}",
    response_model=schemas.Member,
    summary="Read a member",
    description="Read a member with the given id",
)
def read_member(member_id: int, db: Session = Depends(database.get_db)):
    db_member = get_member(db, member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member


@member_router.get(
    "/email/{email}",
    response_model=schemas.Member,
    summary="Read a member by email",
    description="Read a member with the given email",
)
def read_member_by_email(email: str, db: Session = Depends(database.get_db)):
    db_member = get_member_by_email(db, email)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member


@member_router.get(
    "/",
    response_model=List[schemas.Member],
    summary="Read members",
    description="Read members with the given skip and limit",
)
def read_members(
    skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)
):
    log.info(f"Reading members with skip: {skip} and limit: {limit}")
    return get_members(db, skip=skip, limit=limit)


@member_router.put(
    "/{member_id}",
    response_model=schemas.Member,
    summary="Update a member",
    description="Update a member with the given id",
)
def update_existing_member(
    member_id: int, member: schemas.MemberUpdate, db: Session = Depends(database.get_db)
):
    updated_member = update_member(db, member_id, member)
    if updated_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated_member


@member_router.delete(
    "/{member_id}",
    response_model=int,
    summary="Delete a member",
    description="Delete a member with the given id",
)
def delete_existing_member(member_id: int, db: Session = Depends(database.get_db)):
    delete_member(db, member_id)
    return member_id
