# lib/logs.py

from datetime import datetime
from logging import Logger, StreamHandler, FileHandler, Formatter, getLogger
from os.path import join

from assets.config import (
    DATE_FMT,
    LOGGING_LEVEL_LOGGER,
    LOGGING_LEVEL_CONSOLE,
    LOGGING_LEVEL_FILE,
    LOGGING_FORMAT,
    LOG_OUTPUT_PATH,
)
from lib.singletons import Singleton


class CustomLogger(metaclass=Singleton):
    def __init__(
            self,
            console_log: bool = True,
            file_log: bool = False,
            log_level: int = LOGGING_LEVEL_LOGGER,
            file_log_level: int = LOGGING_LEVEL_FILE,
            console_log_level: int = LOGGING_LEVEL_CONSOLE
        ) -> None:
        # variables setup
        date: str = datetime.strftime(datetime.now(), DATE_FMT)
        # logger setup
        self.logger: Logger = getLogger(__name__)
        self.logger.setLevel(level=log_level)
        formatter = Formatter(LOGGING_FORMAT)
        ## console logger setup
        if console_log:
            self.console_log = StreamHandler()
            self.console_log.setLevel(level=console_log_level)
            self.console_log.setFormatter(formatter)
            self.logger.addHandler(self.console_log)
        ## file logger setup
        if file_log:
            log_path = join(LOG_OUTPUT_PATH, f"{date}-execution.log")
            self.file_log = FileHandler(
                filename=log_path,mode="w",
                encoding="latin-1",
                delay=False,
            )
            self.file_log.setLevel(level=file_log_level)
            self.file_log.setFormatter(formatter)
            self.logger.addHandler(self.file_log)
        return None
