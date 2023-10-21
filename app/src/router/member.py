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


@member_router.post("/", response_model=schemas.Member)
def create_new_member(
    member: schemas.MemberCreate, db: Session = Depends(database.get_db)
):
    return create_member(db, member)


@member_router.get("/{member_id}", response_model=schemas.Member)
def read_member(member_id: int, db: Session = Depends(database.get_db)):
    db_member = get_member(db, member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member


@member_router.get("/email/{email}", response_model=schemas.Member)
def read_member_by_email(email: str, db: Session = Depends(database.get_db)):
    db_member = get_member_by_email(db, email)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member


@member_router.get("/", response_model=List[schemas.Member])
def read_members(
    skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)
):
    return get_members(db, skip=skip, limit=limit)


@member_router.put("/{member_id}", response_model=schemas.Member)
def update_existing_member(
    member_id: int, member: schemas.MemberUpdate, db: Session = Depends(database.get_db)
):
    updated_member = update_member(db, member_id, member)
    if updated_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated_member


@member_router.delete("/{member_id}", response_model=int)
def delete_existing_member(member_id: int, db: Session = Depends(database.get_db)):
    delete_member(db, member_id)
    return member_id
