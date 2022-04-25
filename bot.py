import logging
from aiogram import Bot, Dispatcher, executor, types
from decouple import config
from bot_commands import *

# Объект бота
bot = Bot(config('cchbot_token', default=''))
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply('\nИспользуйте команду /menu если хотите узнать, '
                        'что бот может на текущий момент, либо воспользуйтесь '
                        'подсказками при наборе "/" в строке для отправки '
                        'сообщения или, на конец, просто воспользуйтесь '
                        'кнопкой "Меню" - слева, в вышеупомянутой строке')


async def cmd_time(message: types.Message):
    dt_now = str(dt.datetime.now())
    await message.answer(f'Сегодня: {dt_now[:10]}, сейчас: {dt_now[11:-7]}')

dp.register_message_handler(cmd_time, commands="time")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
