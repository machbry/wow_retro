import logging
from logging.config import dictConfig
import yaml
from pathlib import Path

from constants import LOGGER_NAME, WOW_RETRO_CONF_LOGS_PATH


def logging_config_from_yaml(path: Path = WOW_RETRO_CONF_LOGS_PATH) -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f.read())


def init_logger():
    config = logging_config_from_yaml()
    dictConfig(config)


def get_logger():
    return logging.getLogger(name=LOGGER_NAME)
