# --------------------------------------------------------------------------
# TimeTable model의 API router을 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from logging import getLogger
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud import timetable as crud
from src.db import database
from src.schemas import timetable as schemas


log = getLogger(__name__)
timetable_router = APIRouter(prefix="/timetable")


@timetable_router.get(
    "/",
    response_model=List[schemas.TimeTable],
    summary="Read time tables",
    description="Read time tables",
)
async def read_timetables(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(database.get_db)
):
    log.info(f"Reading timetables with skip: {skip} and limit: {limit}")
    return await crud.get_timetables(db, skip=skip, limit=limit)


@timetable_router.get(
    "/{timetable_id}",
    response_model=schemas.TimeTable,
    summary="Read a time table",
    description="Read a time table with the given id",
)
async def read_timetable(
    timetable_id: int, db: AsyncSession = Depends(database.get_db)
):
    db_timetable = await crud.get_timetable(db, timetable_id)
    if db_timetable is None:
        raise HTTPException(status_code=404, detail="TimeTable not found")
    return db_timetable


@timetable_router.post(
    "/",
    response_model=schemas.TimeTable,
    summary="Create a new time table",
    description="Create a new time table with the given name, owner_id, start_date, and end_date",
)
async def create_timetable(
    timetable: schemas.TimeTableCreate, db: AsyncSession = Depends(database.get_db)
):
    return await crud.create_timetable(db, timetable)


@timetable_router.put(
    "/{timetable_id}",
    response_model=schemas.TimeTable,
    summary="Update a time table",
    description="Update a time table with the given name, start_date, and end_date",
)
async def update_timetable(
    timetable_id: int,
    timetable: schemas.TimeTableUpdate,
    db: AsyncSession = Depends(database.get_db),
):
    updated_timetable = await crud.update_timetable(db, timetable_id, timetable)
    if updated_timetable is None:
        raise HTTPException(status_code=404, detail="TimeTable not found")
    return updated_timetable


@timetable_router.delete(
    "/{timetable_id}",
    response_model=int,
    summary="Delete a time table",
    description="Delete a time table with the given id",
)
async def delete_timetable(
    timetable_id: int, db: AsyncSession = Depends(database.get_db)
):
    deleted_timetable_id = await crud.delete_timetable(db, timetable_id)
    if deleted_timetable_id is None:
        raise HTTPException(status_code=404, detail="TimeTable not found")
    return deleted_timetable_id
