# --------------------------------------------------------------------------
# Member model의 CRUD를 담당하는 메서드를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud._base import (
    create_object,
    get_object,
    get_objects,
    delete_object,
    update_object,
)
from src.db.models import Member
from src.schemas import member as schema


async def create_member(db: AsyncSession, member: schema.MemberCreate) -> schema.Member:
    return await create_object(
        db=db, model=Member, obj=member, response_model=schema.Member
    )


async def get_member(db: AsyncSession, member_id: int) -> Optional[schema.Member]:
    return await get_object(
        db=db, model=Member, model_id=member_id, response_model=schema.Member
    )


async def get_member_by_email(db: AsyncSession, email: str) -> Optional[schema.Member]:
    result = await db.execute(select(Member).filter(Member.email == email))  # type: ignore
    member = result.scalar_one_or_none()
    if member:
        return schema.Member.model_validate(member.__dict__)
    return None


async def get_members(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> List[schema.Member]:
    return await get_objects(
        db=db, model=Member, response_model=schema.Member, skip=skip, limit=limit
    )


async def update_member(
    db: AsyncSession, member_id: int, member: schema.MemberUpdate
) -> Optional[schema.Member]:
    return await update_object(
        db=db,
        model=Member,
        model_id=member_id,
        obj=member,
        response_model=schema.Member,
    )


async def delete_member(db: AsyncSession, member_id: int) -> Optional[int]:
    return await delete_object(db=db, model=Member, model_id=member_id)
