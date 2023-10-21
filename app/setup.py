# --------------------------------------------------------------------------
# Backend Application의 패키지 정보를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from setuptools import setup, find_packages

setup(
    name="fastapi-simplebackend",
    description="Simple API server for test",
    author="bnbong",
    author_email="bbbong9@gmail.com",
    packages=find_packages(where="app"),
    use_scm_version=True,
)
