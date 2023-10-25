# --------------------------------------------------------------------------
# Member model의 schema를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from typing import Optional

from pydantic import BaseModel, Field

from src.db.models import Member


class MemberCreate(BaseModel):
    name: str = Field(..., title="Member Name", description="The name of the member.")
    email: str = Field(
        ..., title="Member Email", description="The email address of the member."
    )


class MemberUpdate(BaseModel):
    name: Optional[str] = Field(
        None,
        title="Member Name",
        description="The name of the member. Leave this field empty if you do not want to update it.",
    )
    email: Optional[str] = Field(
        None,
        title="Member Email",
        description="The email address of the member. Leave this field empty if you do not want to update it.",
    )


class Member(BaseModel):  # type: ignore
    id: int = Field(
        ..., title="Member ID", description="The unique identifier of the member."
    )
    name: str = Field(..., title="Member Name", description="The name of the member.")
    email: str = Field(
        ..., title="Member Email", description="The email address of the member."
    )
    items: Optional[list] = Field(
        None,
        title="Member Items",
        description="The items of the member. This field is only available when the member is read.",
    )
    timetables: Optional[list] = Field(
        None,
        title="Member TimeTables",
        description="The timetables of the member. This field is only available when the member is read.",
    )

    class ConfigDict:
        orm_model = Member
        from_attributes = True
