# --------------------------------------------------------------------------
# OpenAPI generator가 읽을 API 문서 내용을 정의하는 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from fastapi import FastAPI


def add_description_at_api_tags(app: FastAPI):
    tag_descriptions = {
        "member": "Member 관련 API. 회원 정보를 관리합니다.",
        "item": "Item 관련 API. 회원의 아이템을 관리합니다.",
        "timetable": "TimeTable 관련 API. 회원의 시간표를 관리합니다.",
    }

    # OpenAPI 태그별 description 생성
    openapi_tags = [
        {"name": tag, "description": desc} for tag, desc in tag_descriptions.items()
    ]

    if app.openapi_tags:
        app.openapi_tags.extend(openapi_tags)
    else:
        app.openapi_tags = openapi_tags
