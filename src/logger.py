import logging
from logging.config import dictConfig
import yaml
from pathlib import Path

from constants import WOW_RETRO_CONF_LOGS_PATH


def logging_config_from_yaml(path: Path = WOW_RETRO_CONF_LOGS_PATH) -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f.read())


class Logger:
    def __init__(self):
        config = logging_config_from_yaml()
        dictConfig(config)
        self._logger = logging.getLogger(name='wowretro')

    def get(self):
        return self._logger
    