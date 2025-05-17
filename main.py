import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, WebAppInfo
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

API_TOKEN = "5662965480:AAEWn7yPAdYWo9_VXmHAWqkMzpvBiPjH728"  # ← bu yerga token yozing

# Botni yaratish
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    user_id = str(message.from_user.id)
    ref = message.text.split(" ")[1] if len(message.text.split()) > 1 else None

    # Mini App tugmasi
    kb = InlineKeyboardBuilder()
    kb.button(
        text="🚀 Mini App’ni ochish",
        web_app=WebAppInfo(
            url=f"https://uzclick.vercel.app/?user_id={user_id}&ref={ref or ''}"
        )
    )

    await message.answer("👋 Assalomu alaykum!\nQuyidagi tugmani bosib Mini App’ni oching:", reply_markup=kb.as_markup())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
