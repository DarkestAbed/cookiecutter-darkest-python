# assets/config.py

from logging import DEBUG, INFO, WARNING, ERROR
from os import getcwd
from os.path import join


# places
PROJECT_PATH: str = getcwd()
ASSETS_FOLDER: str = join(PROJECT_PATH, "assets")
INPUT_FOLDER: str = join(PROJECT_PATH, "inputs")
OUTPUT_FOLDER: str = join(PROJECT_PATH, "outputs")
LOG_OUTPUT: str = join(PROJECT_PATH, "logs")
LOG_OUTPUT_PATH = ""
# formats
LOGGING_FORMAT: str = "%(asctime)s || %(filename)s::%(module)s - %(funcName)s (%(lineno)d) || %(process)d::%(processName)s :: %(levelname)s :: %(message)s"
DATE_FMT: str = ""
# logging
LOGGING_LEVEL_LOGGER: int = DEBUG
LOGGING_LEVEL_CONSOLE: int = INFO
LOGGING_LEVEL_FILE: int = INFO
