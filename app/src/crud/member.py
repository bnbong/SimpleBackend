# --------------------------------------------------------------------------
# Member model의 CRUD를 담당하는 메서드를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from typing import List, Optional

from sqlalchemy.orm import Session

from src.crud._base import (
    create_object,
    get_object,
    get_objects,
    delete_object,
    update_object,
)
from src.db.models import Member
from src.schemas import member as schema


def create_member(db: Session, member: schema.MemberCreate) -> schema.Member:
    return create_object(db, Member, member)


def get_member(db: Session, member_id: int) -> Optional[schema.Member]:
    return get_object(db, Member, member_id)


def get_member_by_email(db: Session, email: str) -> Optional[schema.Member]:
    return db.query(Member).filter(Member.email == email).first()


def get_members(db: Session, skip: int = 0, limit: int = 100) -> List[schema.Member]:
    return get_objects(db, Member, skip, limit)


def update_member(
    db: Session, member_id: int, member: schema.MemberUpdate
) -> schema.Member:
    return update_object(db, Member, member_id, member)


def delete_member(db: Session, member_id: int) -> int:
    return delete_object(db, Member, member_id)
