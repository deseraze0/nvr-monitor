from aiogram import Bot, Dispatcher

from core.config import get_config

config = get_config()

bot = Bot(token=config.telegram.token)
dp = Dispatcher()