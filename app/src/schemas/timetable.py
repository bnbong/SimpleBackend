# --------------------------------------------------------------------------
# TimeTable model의 schema를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from typing import Optional

from pydantic import BaseModel, Field


class TimeTableCreate(BaseModel):
    name: str = Field(
        ..., title="TimeTable Name", description="The name of the timetable."
    )
    owner_id: int = Field(
        ..., title="TimeTable Owner", description="The owner of the timetable."
    )
    start_date: str = Field(
        ...,
        title="TimeTable Start Time",
        description="The start time of the timetable.",
    )
    end_date: str = Field(
        ..., title="TimeTable End Time", description="The end time of the timetable."
    )


class TimeTableUpdate(BaseModel):
    name: Optional[str] = Field(
        None,
        title="TimeTable Name",
        description="The name of the timetable. Leave this field empty if you do not want to update it.",
    )
    start_date: Optional[str] = Field(
        None,
        title="TimeTable Start Time",
        description="The start time of the timetable. Leave this field empty if you do not want to update it.",
    )
    end_date: Optional[str] = Field(
        None,
        title="TimeTable End Time",
        description="The end time of the timetable. Leave this field empty if you do not want to update it.",
    )


class TimeTable(BaseModel):
    id: int = Field(
        ..., title="TimeTable ID", description="The unique identifier of the timetable."
    )
    name: str = Field(
        ..., title="TimeTable Name", description="The name of the timetable."
    )
    owner_id: int = Field(
        ..., title="TimeTable Owner", description="The owner of the timetable."
    )
    start_date: str = Field(
        ...,
        title="TimeTable Start Time",
        description="The start time of the timetable.",
    )
    end_date: str = Field(
        ..., title="TimeTable End Time", description="The end time of the timetable."
    )

    class ConfigDict:
        from_attributes = True
