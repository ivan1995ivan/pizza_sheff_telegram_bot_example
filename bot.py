from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os, json, string


bot = Bot(token='5528768924:AAGjfbIl3owpr3TmE1rj238wEFnEcjemtZE')
dp = Dispatcher(bot)

async def on_startup(_):
	print('Бот вышел в онлайн')
'''###########################################Клиентская часть##################################################'''
@dp.message_handler(commands=['start','help'])
async def comands_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id,'Приятного апетита')
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_Sheef_test_1Bot')

@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 9.00 до 20.00, Пт-Сб с 10.00 до 23.00')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'ул. Проездная 26')

'''#############################################Общая часть##########################################################'''

@dp.message_handler()
async def echo_send(message : types.Message):
	if {i.lower().translate(str.maketrans('','', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(set(json.load(open('cenz.json')))) != set():
		await message.reply('Маты запрещены')
		await message.delete()
	

executor.start_polling(dp, skip_updates=True,on_startup=on_startup)