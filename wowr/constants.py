import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

WOWR_CONF_DIRECTORY_PATH = Path(os.environ["WOWR_CONF_DIRECTORY_PATH"]).resolve()
WOWR_CONF_LOGS_PATH = WOWR_CONF_DIRECTORY_PATH / "logs.yaml"
WOWR_LOGGER_NAME = os.environ["WOWR_LOGGER_NAME"]

WOWR_DATA_DIRECTORY_PATH = Path(os.environ["WOWR_DATA_DIRECTORY_PATH"]).resolve()
WOWR_DATA_DIRECTORY_PATH.mkdir(parents=True, exist_ok=True)

WLOGS_CLIENT_ID = os.environ["WLOGS_CLIENT_ID"]
WLOGS_CLIENT_SECRET = os.environ["WLOGS_CLIENT_SECRET"]
WLOGS_TOKEN_URL = os.environ["WLOGS_TOKEN_URL"]
WLOGS_AUTHORIZE_URL = os.environ["WLOGS_AUTHORIZE_URL"]
WLOG_AUTH_FLOW_DATA = {'grant_type': os.environ["WLOGS_GRANT_TYPE"]}

WOWR_GUILD_ID = os.environ["WOWR_GUILD_ID"]
WOWR_DEFAULT_ZONE_ID = os.environ["WOWR_DEFAULT_ZONE_ID"]