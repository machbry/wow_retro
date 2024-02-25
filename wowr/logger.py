import logging
from logging.config import dictConfig
import yaml
from pathlib import Path

from constants import WOWR_LOGGER_NAME, WOWR_CONF_LOGS_PATH


def logging_config_from_yaml(path: Path = WOWR_CONF_LOGS_PATH) -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f.read())


def init_logger():
    config = logging_config_from_yaml()
    dictConfig(config)


def get_logger():
    return logging.getLogger(name=WOWR_LOGGER_NAME)
