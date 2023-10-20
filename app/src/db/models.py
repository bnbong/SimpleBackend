from sqlalchemy import Integer, String, Column

from src.db._base import ModelBase


class Member(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
