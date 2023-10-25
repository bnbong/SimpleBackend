# --------------------------------------------------------------------------
# TimeTable model의 CRUD를 담당하는 메서드를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.crud._base import (
    create_object,
    get_object,
    get_objects,
    delete_object,
    update_object,
)
from src.db.models import TimeTable
from src.schemas import timetable as schema


async def create_timetable(
    db: AsyncSession, timetable: schema.TimeTableCreate
) -> schema.TimeTable:
    return await create_object(
        db=db, model=TimeTable, obj=timetable, response_model=schema.TimeTable
    )


async def get_timetable(
    db: AsyncSession, timetable_id: int
) -> Optional[schema.TimeTable]:
    return await get_object(
        db=db, model=TimeTable, model_id=timetable_id, response_model=schema.TimeTable
    )


async def get_timetables(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> List[schema.TimeTable]:
    return await get_objects(
        db=db, model=TimeTable, response_model=schema.TimeTable, skip=skip, limit=limit
    )


async def update_timetable(
    db: AsyncSession, timetable_id: int, timetable: schema.TimeTableUpdate
) -> Optional[schema.TimeTable]:
    return await update_object(
        db=db,
        model=TimeTable,
        model_id=timetable_id,
        obj=timetable,
        response_model=schema.TimeTable,
    )


async def delete_timetable(db: AsyncSession, timetable_id: int) -> Optional[int]:
    return await delete_object(db=db, model=TimeTable, model_id=timetable_id)
