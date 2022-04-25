import logging
from aiogram import Bot, Dispatcher, executor, types
from decouple import config

# Объект бота
bot = Bot(config('cchbot_token', default=''))
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply('\nИспользуйте комманду /menu если хотите узнать, что бот может на текущий момент, либо '
            'воспользуётесь подсказками при наборе "/" в строке для отправки сообщения или, на конец, '
            'просто воспользуйтесь кнопкой "Меню" - слева, в вышеупомянутой строке')


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
