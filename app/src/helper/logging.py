import os
import sys
import logging
import logging.handlers

from src.core.settings import AppSettings


LOGGING_FORMAT = (
    "[%(levelname)1.1s "
    "%(asctime)s "
    "P%(process)d "
    "%(threadName)s "
    "%(module)s:%(lineno)d] "
    "%(message)s"
)


def init_logger(root_logger_name: str, app_settings: AppSettings) -> logging.Logger:
    app_logger_level = (
        logging.DEBUG if app_settings.LOGGING_DEBUG_LEVEL else logging.INFO
    )

    app_logger = logging.getLogger(root_logger_name)
    app_logger.setLevel(app_logger_level)

    # STDOUT handler
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(app_logger_level)
    stdout_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))

    # File handler
    log_file_path = "app.log"
    if hasattr(app_settings, 'LOG_FILE_PATH'):
        log_file_path = app_settings.LOG_FILE_PATH

    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(app_logger_level)
    file_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    app_logger.addHandler(file_handler)

    app_logger.info("App logger is started.")

    return app_logger
