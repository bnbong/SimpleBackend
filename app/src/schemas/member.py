# --------------------------------------------------------------------------
# Member model의 schema를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from typing import Optional

from pydantic import BaseModel


class MemberCreate(BaseModel):
    name: str
    email: str


class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


class Member(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
