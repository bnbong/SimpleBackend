# --------------------------------------------------------------------------
# FastAPI Application을 생성하는 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from __future__ import annotations

import logging

from fastapi import FastAPI
from setuptools_scm import get_version

from src.helper.logging import init_logger as _init_logger
from src.router import router
from src.core.settings import AppSettings

__version__ = get_version(root="../..", relative_to=__file__)


logger = logging.getLogger(__name__)


def init_logger(app_settings: AppSettings) -> None:
    _init_logger(f"fastapi-backend@{__version__}", app_settings)


def create_app(app_settings: AppSettings) -> FastAPI:
    app = FastAPI()

    app.include_router(router)

    @app.on_event("startup")
    async def startup_event():
        logger.info("Application startup")

    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("Application shutdown")

    return app
