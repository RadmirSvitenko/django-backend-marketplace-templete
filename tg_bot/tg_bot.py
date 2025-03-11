import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv

# Это тестовый бот телеграмм, пробую новую библиотеку

# Указываем токен бота
load_dotenv()
TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаём объект бота и диспетчера
bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()

# Создаем клавиатуру с кнопками
def get_main_menu():
    keyword = ReplyKeyboardMarkup(resize_keyboard=True)
    buttonStart = KeyboardButton('Старт ')
    buttonMenu = KeyboardButton('Меню 👀')
    buttonSettings = KeyboardButton('Настройки 🦾')
    buttonExit = KeyboardButton('Выход 🙅‍♂️')
    keyword.add(buttonStart, buttonMenu, buttonSettings, buttonExit)
    return keyword


# Команда START
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я твой Telegram-бот 😄")
    await message.answer('Выберите действие: ', reply_markup=menu)

# Команда HELP
@dp.message(Command("help"))
async def help_messege(message: Message):
    await message.answer("Вот список команд: \n/start - Запуск бота\n/help - список команд\n", reply_markup=menu)

# Запуск бота
async def main():
    await dp.start_polling(bot)

# Создаём клавиатуру
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🖖 Старт")],
        [KeyboardButton(text="📋 Меню")],
        [KeyboardButton(text="ℹ️ О нас")],
        [KeyboardButton(text="⚙️ Настройки")],
        [KeyboardButton(text="😔 Выход")],
    ],
    resize_keyboard=True  # Автоизменение размера
)

@dp.message()
async def button_handler(message: Message):
    # Проверяем, какой текст был нажат на кнопке
    if message.text == "🖖 Старт":
        await message.answer("Вы нажали кнопку '🖖 Старт'")
    elif message.text == "📋 Меню":
        await message.answer("Вы нажали кнопку '📋 Меню'")
    elif message.text == "ℹ️ О нас":
        await message.answer("Вы нажали кнопку 'ℹ️ О нас'")
    elif message.text == "⚙️ Настройки":
        await message.answer("Вы нажали кнопку '⚙️ Настройки'")

if __name__ == '__main__':
    asyncio.run(main())