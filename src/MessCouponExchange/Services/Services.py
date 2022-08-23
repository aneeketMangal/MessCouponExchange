import os
import telebot
from src.MessCouponExchange.Database import DatabaseProvider

from dotenv import load_dotenv

load_dotenv()
BOT_INSTANCE = telebot.TeleBot(os.getenv('API_KEY'), parse_mode=None)
DB_INSTANCE = DatabaseProvider(os.getenv('MONGO_URI'))
