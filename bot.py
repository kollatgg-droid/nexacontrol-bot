import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "ВСТАВЬ_СЮДА_ТОКЕН"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Бот работает ⚡")

@dp.message_handler(commands=["promote"])
async def promote(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Ответь на пользователя")
        return

    user_id = message.reply_to_message.from_user.id

    await bot.promote_chat_member(
        chat_id=message.chat.id,
        user_id=user_id,
        can_manage_chat=True,
        can_delete_messages=True,
        can_invite_users=True
    )

    await message.reply("Пользователь повышен ✅")

if __name__ == "__main__":
    executor.start_polling(dp)