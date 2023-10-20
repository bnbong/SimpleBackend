from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import AnyUrl, BaseSettings, Field


class AppSettings(BaseSettings):
    LOGGING_DEBUG_LEVEL: bool = Field(
        default=True,
        description="True: DEBUG mode, False:: INFO mode",
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
        default="mysql+pymysql://fastapi:devpassword@localhost:3306/fastapidb",
        description="MariaDB connection URI.",
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

    class Config:
        env_file = ".env"
        env_prefix = "fastapiapp_"
