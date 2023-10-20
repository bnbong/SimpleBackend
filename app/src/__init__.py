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

    return app
