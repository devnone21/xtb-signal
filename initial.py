import os
import json
import logging.config
from classes import Settings
from dotenv import load_dotenv

load_dotenv()

_logging_json = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default"
        },
        "rotating": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "default",
            "filename": os.getenv("LOG_PATH", default="app.log"),
            "when": "midnight",
            "backupCount": 3
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "CRITICAL",
            "propagate": True
        },
        "xtb": {
            "handlers": ["rotating"],
            "level": "DEBUG"
        }
    }
}
logging.config.dictConfig(_logging_json)

accounts: dict = json.load(open('account.json'))

ind_presets = {
    "TA_RSI_L14_XA70_XB30": [
        {
            "kind": "rsi", "length": 14, "signal_indicators": True,
            "xa": 70, "xb": 30
        }
    ],
    "TA_RSI_L14_XA65_XB35": [
        {
            "kind": "rsi", "length": 14, "signal_indicators": True,
            "xa": 65, "xb": 35
        }
    ],
    "TA_STOCH_K14_XA80_XB20": [
        {
            "kind": "stoch", "k": 14, "d": 3, "smooth_k": 3,
            "xa": 80, "xb": 20
        }
    ],
    "TA_MACD_F10_S25": [
        {
            "kind": "macd", "fast": 10, "slow": 25, "signal_indicators": True
        }
    ],
    "TA_MACD_F10_S50": [
        {
            "kind": "macd", "fast": 10, "slow": 50, "signal_indicators": True
        }
    ],
    "TA_MACD_F25_S50": [
        {
            "kind": "macd", "fast": 25, "slow": 50, "signal_indicators": True
        }
    ],
}

# Uncomment if KV settings is used
# _kv = KV()
# settings = Settings(**_kv.query())

# Uncomment if local settings is used
settings = Settings(**json.load(open('settings.json')))

if __name__ == '__main__':
    print(settings.profiles)
