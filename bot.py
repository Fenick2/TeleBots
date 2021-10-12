import os
from yobit import get_btc_eth
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv


load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await message.reply('Привет!\nНапиши или нажми "/rate" и я пришлю тебе текущий курс Биткоина и Эфира!')


@dp.message_handler(commands=['rate', 'курс'])
async def btc_level(message: types.Message):
    try:
        await message.reply(f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f'*** Текущий курс: ***\n{get_btc_eth()}'
                            )
    except:
        await message.reply('\U00002620 Ошибочка! Повтори попозже. \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
