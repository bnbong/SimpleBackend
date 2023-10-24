# --------------------------------------------------------------------------
# Backend Application의 설정을 관리하는 파일입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    LOGGING_DEBUG_LEVEL: bool = Field(
        default=True,
        description="True: DEBUG mode, False:: INFO mode",
    )
    LOG_FILE_PATH: str = Field(
        default="../logs/app.log",
        description="Log file path",
    )
    DEBUG_ALLOW_CORS_ALL_ORIGIN: bool = Field(
        default=True,
        description="If True, allow origins for CORS requests.",
    )
    DEBUG_ALLOW_NON_CERTIFICATED_USER_GET_TOKEN: bool = Field(
        default=True,
        description="If True, allow non-cerficiated users to get ESP token.",
    )

    THREAD_POOL_SIZE: Optional[int] = Field(
        default=10,
        description="Change the server's thread pool size to handle non-async function",
    )

    SECRET_KEY: str = Field(
        default="example_secret_key_WoW",
        description="Secret key to be used for issuing HMAC tokens.",
    )

    DATABASE_URI: AnyUrl = Field(
        default="mysql+pymysql://bnbong:password@localhost:3306/fastapidb",
        description="MariaDB connection URI.",
    )
    TEST_DATABASE_URL: AnyUrl = Field(
        default="mysql+pymysql://bnbong:password@localhost:3306/fastapidb_test",
        description="MariaDB connection URI for test.",
    )
    DATABASE_OPTIONS: Dict[str, Any] = Field(
        default={
            "pool_size": 10,
            "max_overflow": 20,
            "pool_recycle": 300,
            "pool_pre_ping": True,
        },
        description="MariaDB option to create a connection.",
    )

    class ConfigDict:
        env_file = ".env"
