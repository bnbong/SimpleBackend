from sqlalchemy import Integer, String, Column

from src.db._base import ModelBase


class Member(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), index=True)
    email = Column(String(length=255), unique=True, index=True)
