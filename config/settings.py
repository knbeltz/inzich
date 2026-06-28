"""Loads and validates all environment configuration for the application."""

import os 
from pathlib import Path
from dotenv import load_dotenv 

loaded = load_dotenv()

if loaded is False: 
   raise ValueError(".env file is missing. Add a .env file and try again.")

def _require_env(key: str) -> str: 
   value = os.getenv(key)
   if value is None or value == "":
      raise ValueError(f"Missing required environment variable: {key}. To fix it, copy and paste the .env.example as a .env file.")
   return value

OPENAI_API_KEY = _require_env("OPENAI_API_KEY")
DB_PATH = Path(_require_env("DB_PATH"))
EXPORT_DIR = Path(_require_env("EXPORT_DIR"))

EXPORT_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH.parent.mkdir(parents=True, exist_ok=True)



