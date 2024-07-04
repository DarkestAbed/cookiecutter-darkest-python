# lib/read_env.py

from dotenv import load_dotenv
from os import environ
from os.path import exists

from assets.config import ENV_LOC_LOCAL, LOGGING_LEVEL_LOGGER
from lib.logs import CustomLogger

logs: CustomLogger = CustomLogger(
    console_log=True,
    file_log=False,
    log_level=LOGGING_LEVEL_LOGGER,
)
plog = logs.logger


def read_env_file(file_loc: str | None = None, strict: bool = True) -> None:
    # checking .env location
    if file_loc is None:
        if exists(ENV_LOC_LOCAL):
            env_loc = ENV_LOC_LOCAL
        else:
            if strict:
                try:
                    env_var_test = environ.get("ENVIRON", None)
                    plog.debug(f"{env_var_test = }")
                    if (env_var_test is None):
                        raise FileNotFoundError
                    else:
                        plog.warning("Environment variables located. Proceeding...")
                        return None
                except AttributeError:
                    raise FileNotFoundError
    else:
        env_loc = file_loc
    # checking if env file exists
    if exists(env_loc):
        load_dotenv(dotenv_path=env_loc)
    else:
        if strict:
            raise FileNotFoundError
        else:
            plog.warning("No environment file located. Proceeding...")
            return None
    # checking if env vars are populated
    user_tmp = environ.get("ENVIRON", None)
    if user_tmp is None:
        if strict:
            raise FileNotFoundError
        else:
            plog.warning("No environment variables found. Proceeding...")
    return None


def read_env_remote(environment: str = "dev", project: str = "rutificador") -> None:
    ...
    return None
