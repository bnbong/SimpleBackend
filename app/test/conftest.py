import asyncio

import uvloop
import pytest
import pytest_asyncio

from typing import AsyncGenerator, Iterator, AsyncIterator
from asyncio import AbstractEventLoop
from asgi_lifespan import LifespanManager

from fastapi import FastAPI, Depends
from httpx import AsyncClient

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession

from helper import get_test_engine
from src.db.database import Base, get_db
from src.core.settings import AppSettings
from src import create_app


# @pytest.fixture(scope="class")
# def event_loop() -> Iterator[AbstractEventLoop]:
#     loop = uvloop.new_event_loop()
#     yield loop
#     loop.close()


# @pytest.fixture(scope="session")
# def event_loop():
#     loop = asyncio.new_event_loop()
#     yield loop
#     loop.close()
#
#
# @pytest.fixture(scope="session", autouse=True)
# def setup_uvloop():
#     uvloop.install()
#
#
# @pytest_asyncio.fixture(scope="session", autouse=True)
# def async_engine():
#     engine = create_async_engine(str(settings.TEST_DATABASE_URL), **settings.DATABASE_OPTIONS)
#     return engine
#
#
# @pytest_asyncio.fixture(scope="session")
# async def async_session(async_engine):
#     async_session_cls = sessionmaker(  # type: ignore
#         bind=async_engine, class_=AsyncSession, expire_on_commit=False
#     )
#     async with async_session_cls() as session:
#         yield session
#
#
# @pytest_asyncio.fixture(scope="session")
# async def init_db(async_engine):
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
#
# @pytest_asyncio.fixture(scope="class")
# def app(init_db) -> FastAPI:
#     from src import create_app
#
#     app = create_app(settings)
#     app.dependency_overrides[get_db] = async_session
#
#     return app
#
#
# @pytest_asyncio.fixture(scope="class")
# async def client(app: FastAPI):
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         yield ac
@pytest.fixture(scope="session")
def async_engine(app_settings: AppSettings):
    engine = create_async_engine(
        str(app_settings.TEST_DATABASE_URL), **app_settings.DATABASE_OPTIONS
    )
    return engine


@pytest.fixture(scope="session")
async def async_session(app_settings: AppSettings):
    async_session_cls = sessionmaker(  # type: ignore
        bind=async_engine(app_settings), class_=AsyncSession, expire_on_commit=False
    )
    async with async_session_cls() as session:
        yield session


# @pytest_asyncio.fixture(scope="session", autouse=True)
async def init_db(async_engine: AsyncEngine):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="session")
def app_settings() -> AppSettings:
    # return AppSettings(_env_file=".env.test")
    return AppSettings()


@pytest.fixture(scope="class")
def event_loop() -> Iterator[AbstractEventLoop]:
    loop = uvloop.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="class")
async def app_client(app_settings: AppSettings) -> AsyncIterator[AsyncClient]:
    app = create_app(app_settings)
    app.dependency_overrides[get_db] = async_session
    async with AsyncClient(
        app=app, base_url="http://test"
    ) as app_client, LifespanManager(app):
        yield app_client
