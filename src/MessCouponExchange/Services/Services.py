import os
import telebot
from telebot import apihelper
from src.MessCouponExchange.Database import DatabaseProvider

from dotenv import load_dotenv

load_dotenv()
# apihelper.proxy = {'http': TG_PROXY}
BOT_INSTANCE = telebot.TeleBot(os.getenv('API_KEY'), parse_mode=None)
DB_INSTANCE = DatabaseProvider(os.getenv('MONGO_URI'))
