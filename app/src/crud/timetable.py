# --------------------------------------------------------------------------
# TimeTable model의 CRUD를 담당하는 메서드를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from sqlalchemy.orm import Session

from src.crud._base import (
    create_object,
    get_object,
    get_objects,
    delete_object,
    update_object,
)
from src.db.models import TimeTable
from src.schemas.timetable import TimeTableCreate


def create_timetable(db: Session, timetable: TimeTableCreate) -> TimeTable:
    return create_object(db, TimeTable, timetable)


def get_timetable(db: Session, timetable_id: int) -> TimeTable:
    return get_object(db, TimeTable, timetable_id)


def get_timetables(db: Session, skip: int = 0, limit: int = 100) -> TimeTable:
    return get_objects(db, TimeTable, skip, limit)


def update_timetable(db: Session, timetable_id: int, timetable: TimeTable) -> TimeTable:
    return update_object(db, TimeTable, timetable_id, timetable)


def delete_timetable(db: Session, timetable_id: int) -> int:
    return delete_object(db, TimeTable, timetable_id)
