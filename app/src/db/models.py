# TODO: item model을 정의 및 관련 CRUD 구현.
# --------------------------------------------------------------------------
# Member model을 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from sqlalchemy import Integer, String, Column

from src.db._base import ModelBase


class Member(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), index=True)
    email = Column(String(length=255), unique=True, index=True)
