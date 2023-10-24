# --------------------------------------------------------------------------
# FastAPI Application을 생성하는 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from __future__ import annotations

import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager
from setuptools_scm import get_version

from src.helper.logging import init_logger as _init_logger
from src.router import router
from src.core.settings import AppSettings
from src.utils.documents import add_description_at_api_tags

__version__ = get_version(root="../..", relative_to=__file__)


logger = logging.getLogger(__name__)


def init_logger(app_settings: AppSettings) -> None:
    _init_logger(f"fastapi-backend@{__version__}", app_settings)


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    try:
        logger.info("Application startup")
        yield
    finally:
        logger.info("Application shutdown")


def create_app(app_settings: AppSettings) -> FastAPI:
    app = FastAPI(
        title="Simple Backend API",
        description="Simple Backend Application using FastAPI",
        version=__version__,
    )

    app.include_router(router)

    add_description_at_api_tags(app)

    return app
