from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()

class Config(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_ADMIN_ID: str
    TELEGRAM_ADMIN_USERNAME: str
    GROQ_API_KEY: str
    TELEGRAM_CHAT_HISTORY_DB_PATH: str

config = Config()