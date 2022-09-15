from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

bot = Bot(token='5528768924:AAGjfbIl3owpr3TmE1rj238wEFnEcjemtZE')
dp = Dispatcher(bot, storage=storage)
