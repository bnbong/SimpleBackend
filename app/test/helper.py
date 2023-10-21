from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.settings import AppSettings


def get_test_engine() -> create_engine:
    settings = AppSettings()
    engine = create_engine(str(settings.TEST_DATABASE_URL), **settings.DATABASE_OPTIONS)

    return engine


def override_get_db():
    db = sessionmaker(bind=get_test_engine())()
    try:
        yield db
    finally:
        db.close()
