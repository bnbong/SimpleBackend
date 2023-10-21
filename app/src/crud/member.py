# --------------------------------------------------------------------------
# Member model의 CRUD를 담당하는 메서드를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from typing import List, Optional

from sqlalchemy.orm import Session

from src.db.models import Member
from src.schemas.member import MemberCreate, MemberUpdate


def create_member(db: Session, member: MemberCreate) -> Member:
    db_member = Member(**member.model_dump())

    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def get_member(db: Session, member_id: int) -> Optional[Member]:
    return db.query(Member).filter(Member.id == member_id).first()


def get_member_by_email(db: Session, email: str) -> Optional[Member]:
    return db.query(Member).filter(Member.email == email).first()


def get_members(db: Session, skip: int = 0, limit: int = 100) -> List[Member]:
    return db.query(Member).offset(skip).limit(limit).all()


def update_member(db: Session, member_id: int, member: MemberUpdate) -> Member:
    db_member = db.query(Member).filter(Member.id == member_id).first()
    update_data = member.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_member, key, value)

    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def delete_member(db: Session, member_id: int) -> int:
    db.query(Member).filter(Member.id == member_id).delete()
    db.commit()
    return member_id
