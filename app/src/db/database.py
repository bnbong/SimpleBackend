from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from pydantic import AnyUrl

from src.core.settings import AppSettings


settings = AppSettings()

SQLALCHEMY_DATABASE_URL: AnyUrl = settings.DATABASE_URI
engine_options = settings.DATABASE_OPTIONS

engine = create_engine(SQLALCHEMY_DATABASE_URL, **engine_options)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
