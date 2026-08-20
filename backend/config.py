import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    TELEBOT_TOKEN = os.getenv("TELEBOT_TOKEN")
    
    ADMIN_ID = os.getenv("ADMIN_ID")
    
    COMMANDS = {
        "/start": "Краткая информация и начало диалога",
        "/reg": "Регистрация"
    }

    DATABASE_PATH = "data/users.db"


config = Config()