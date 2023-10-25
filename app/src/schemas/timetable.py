# --------------------------------------------------------------------------
# TimeTable model의 schema를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from typing import Optional
from datetime import date

from pydantic import BaseModel, Field

from src.db.models import TimeTable


class TimeTableCreate(BaseModel):
    index: str = Field(
        ..., title="TimeTable Index", description="The description of the timetable."
    )
    owner_id: int = Field(
        ..., title="TimeTable Owner", description="The owner of the timetable."
    )
    start_date: date = Field(
        ...,
        title="TimeTable Start Time",
        description="The start time of the timetable.",
        json_schema_extra={"format": "%Y-%m-%d"}
    )
    end_date: date = Field(
        ...,
        title="TimeTable End Time",
        description="The end time of the timetable.",
        json_schema_extra={"format": "%Y-%m-%d"}
    )


class TimeTableUpdate(BaseModel):
    index: Optional[str] = Field(
        None,
        title="TimeTable Index",
        description="The description of the timetable. Leave this field empty if you do not want to update it.",
    )
    start_date: Optional[date] = Field(
        None,
        title="TimeTable Start Time",
        description="The start time of the timetable. Leave this field empty if you do not want to update it.",
        json_schema_extra={"format": "%Y-%m-%d"}
    )
    end_date: Optional[date] = Field(
        None,
        title="TimeTable End Time",
        description="The end time of the timetable. Leave this field empty if you do not want to update it.",
        json_schema_extra={"format": "%Y-%m-%d"}
    )


class TimeTable(BaseModel):  # type: ignore
    id: int = Field(
        ..., title="TimeTable ID", description="The unique identifier of the timetable."
    )
    index: str = Field(
        ..., title="TimeTable Index", description="The description of the timetable."
    )
    owner_id: int = Field(
        ..., title="TimeTable Owner", description="The owner of the timetable."
    )
    start_date: date = Field(
        ...,
        title="TimeTable Start Time",
        description="The start time of the timetable.",
        json_schema_extra={"format": "%Y-%m-%d"}
    )
    end_date: date = Field(
        ...,
        title="TimeTable End Time",
        description="The end time of the timetable.",
        json_schema_extra={"format": "%Y-%m-%d"}
    )

    class ConfigDict:
        orm_model = TimeTable
        from_attributes = True
