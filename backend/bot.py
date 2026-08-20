from telebot import TeleBot
from .config import config

bot = TeleBot(config.TELEBOT_TOKEN)