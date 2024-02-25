import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

LOGGER_NAME = "wowretro"

WOW_RETRO_SRC_PATH = Path(__name__).parent
WOW_RETRO_CONF_LOGS_PATH = WOW_RETRO_SRC_PATH / "conf/logs.yaml"

WLOGS_CLIENT_ID = os.environ["WLOGS_CLIENT_ID"]
WLOGS_CLIENT_SECRET = os.environ["WLOGS_CLIENT_SECRET"]
WLOGS_TOKEN_URL = os.environ["WLOGS_TOKEN_URL"]
WLOGS_AUTHORIZE_URL = os.environ["WLOGS_AUTHORIZE_URL"]
WLOG_AUTH_FLOW_DATA = {'grant_type': os.environ["WLOGS_GRANT_TYPE"]}

WOW_GUILD_ID = os.environ["WOW_GUILD_ID"]
WOW_DEFAULT_ZONE_ID = os.environ["WOW_DEFAULT_ZONE_ID"]
