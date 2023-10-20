from pydantic import BaseModel


class MemberCreate(BaseModel):
    name: str
    email: str


class MemberUpdate(BaseModel):
    name: str
    email: str


class Member(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
