from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

WOW_RETRO_SRC_PATH = Path(__name__).parent
WOW_RETRO_CONF_LOGS_PATH = WOW_RETRO_SRC_PATH / "conf/logs.yaml"
