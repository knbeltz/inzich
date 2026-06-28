"""Configures the application's logger to write logs to both the console and a log file."""

import logging 
from pathlib import Path 

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True) 

logger = logging.getLogger("inzich") 
logger.setLevel(logging.DEBUG) 

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

try:
    file_handler = logging.FileHandler(LOGS_DIR / "inzich.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
except Exception:
    pass 

stream_handler = logging.StreamHandler() 
stream_handler.setLevel(logging.INFO) 
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler) 




