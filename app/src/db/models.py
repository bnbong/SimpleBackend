# --------------------------------------------------------------------------
# Member model을 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from sqlalchemy import Integer, String, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.db._base import ModelBase


class Member(ModelBase):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=255), index=True)
    email = Column(String(length=255), unique=True, index=True)

    items = relationship("Item", back_populates="owner")
    timetables = relationship("TimeTable", back_populates="owner")


class Item(ModelBase):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=255), index=True)
    price = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("member.id"))

    owner = relationship("Member", back_populates="items")


class TimeTable(ModelBase):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    index = Column(String(length=1024), index=True)
    owner_id = Column(Integer, ForeignKey("member.id"))
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))

    owner = relationship("Member", back_populates="timetables")
