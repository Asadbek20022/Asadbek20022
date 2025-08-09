from pydoc import text
import time
import re  # 🔹 REGEX uchun: so‘zlarni aniq ajratish
from telegram import ChatPermissions, Update, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from aiogram.client import bot
from telegram import Update, ChatPermissions
from telegram.ext import (
    ApplicationBuilder, MessageHandler, ChatMemberHandler,
    ContextTypes, CommandHandler, filters
)
from telegram.ext import filters  # <<<< BU QATOR SHU YERGA KERAK
from deep_translator import GoogleTranslator
from telegram import Update
from telegram.ext import ContextTypes


BAD_WORDS = ["fuck", "ko't", "gandon", "dnx", "haromi", "g‘irt", "foxsha",  "sikaman", "oneni", "openi", "dadeni", "onen", "seks", "😒", "🐵", "🙈", "🙉", "🙊", "🐒", "🧔", "🌟", "🔥", "xunuk", "pastkash",
    "yban", "qo'toq", "qotoq", "shayton", "tupoy","siydik", "bo'q", "tashoq", "sex", "sexs", "boshini yebdi", "xxx", "mashka", "Mashka", "dalbayob", "kallenga", "gandon", "suka"]  # kengaytiriladi

REKLAMA_SOZLAR = ["http", "https", "t.me", "link"]  # <<< SHU QATOR KERAK

user_warnings = {}  # har bir foydalanuvchi uchun ogohlantirishlar hisoblagichi

# Kalit so'z va havolalar
LINKS = {
    "uc": "https://t.me/SLARKuc/248",
    "stars": "https://t.me/SLARKuc/249",
    "admin": "@vipASADEK",
    "telegram stars": "https://t.me/SLARKuc/249",
    "premium": "https://t.me/SLARKuc/250",
    "donat": "https://t.me/SLARKuc/251",
    "korea": "https://t.me/SLARKuc/253",
    "korea pubg": "https://t.me/SLARKuc/253",
    "uc narx": "https://t.me/SLARKuc/254",
    "porno": "https://t.me/SLARK_MOVIE/221",
    "uc narxlari": "https://t.me/SLARKuc/254",
    "akk ichidan": "https://t.me/SLARKuc/256",
    "dls": "https://t.me/SLARKuc/257",
    "dls 2025": "https://t.me/SLARKuc/257",
    "ml": "https://t.me/SLARKuc/258",
    "mobile legends": "https://t.me/SLARKuc/258",
    "ff": "https://t.me/SLARKuc/259",
    "free fire": "https://t.me/SLARKuc/259",
    "brawl stars": "https://t.me/SLARKuc/260",
    "tiktok": "https://t.me/SLARKuc/261",
    "tiktok coins": "https://t.me/SLARKuc/261",
    "kino": "@slark_movie",
    "nakrutka": "https://t.me/SLARK_NAKRUTKA",
}

# === START komandasi ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Men Madina botman 😊\n"
        "Mendan foydalanish uchun meni guruhingizga qo‘shing va admin bering.\n"
        "Men guruhingizni reklama va yomon so‘zlardan tozalayman."
    )

# === Guruhga kirganda salomlashish ===
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"👋 Salom, {member.full_name}! Xush kelibsiz!")

# === Ijtimoiy tarmoqlar uchun tugmalar ===
def get_kino_buttons():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Kino Kanal", url="https://t.me/SLARK_MOVIE")
        ]
    ])

# === 3 soatda faollik eslatmasi yuboruvchi ===
async def eslatma_berish(bot, chat_id):
    while True:
        try:
            await bot.send_message(
                chat_id,
                "zerikdingizmi! \n"
            "unda bizning kino kanalga obuna bo‘ling\n"
            "va yangi filmlar haqida xabardor bo‘ling",
                reply_markup=get_kino_buttons()
            )
            await asyncio.sleep(10800)  # 3 soat
        except Exception as e:
            print(f"Reklama xatosi: {e}")
            await asyncio.sleep(60)

# === Ijtimoiy tarmoqlar uchun tugmalar ===
def get_uc_buttons():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Narxlar", url="https://t.me/SLARKuc")
        ]
    ])

# === 5 soatda faollik eslatmasi yuboruvchi ===
async def faollik_eslatma(bot, chat_id):
    while True:
        try:
            await bot.send_message(
                chat_id,
                "kimga arzon ishonchlik tezkor uc, stars\n"
                 "va premium kerak bolsa 👇",
                reply_markup=get_uc_buttons()
            )
            await asyncio.sleep(18000)  # 5 soat
        except Exception as e:
            print(f"Reklama xatosi: {e}")
            await asyncio.sleep(60)

# === Ijtimoiy tarmoqlar uchun tugmalar ===
def get_social_buttons():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📱 Instagram", url="https://www.instagram.com/slark_moviebot"),
            InlineKeyboardButton(text="🔴 YouTube", url="https://youtube.com/@slarkpubg?feature=shared")
        ],
        [
            InlineKeyboardButton(text="⚫️ TikTok", url="https://www.tiktok.com/@slark_movie?_t=ZS-8y23AY8uAID&_r=1"),
            InlineKeyboardButton(text="🎬 Kino Kanal", url="https://t.me/SLARK_MOVIE")
        ],
        [
            InlineKeyboardButton(text="📣Accaunt reklama qilish", url="https://t.me/vipASADBEK")
        ]
    ])

# === Ijtimoiy tarmoqlar uchun tugmalar ===
async def avtomatik_reklama(bot, chat_id):
    while True:
        try:
            await bot.send_message(
                chat_id,
                "📣 Bizning ijtimoiy sahifalarimizga obuna\n"
                 "bo‘ling yangiliklar birinchi shu yerda 👇",
                reply_markup=get_social_buttons()
            )
            await asyncio.sleep(21600)  # 6 soat
        except Exception as e:
            print(f"Reklama xatosi: {e}")
            await asyncio.sleep(60)

# === Bot ishga tushganda avtomatik eslatmalar ===
async def on_start(app):
    bot = app.bot

    # Har xil eslatmalar uchun har xil guruhlar
    eslatma_chat_id = -1001806140561        # ← faqat eslatma uchun guruh ID
    faollik_chat_id = -1001806140561        # ← faqat faollik uchun guruh ID
    reklama_chat_id = -1001806140561        # ← faqat reklama uchun guruh ID

    asyncio.create_task(eslatma_berish(bot, eslatma_chat_id))
    asyncio.create_task(faollik_eslatma(bot, faollik_chat_id))
    asyncio.create_task(avtomatik_reklama(bot, reklama_chat_id))


# === Barcha vazifalarni bajaruvchi master handler ===
async def master_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global user_warnings

    if update.message is None or update.message.text is None:
        return

    text = update.message.text.lower()
    words = text.split()
    user_id = update.message.from_user.id
    chat_id = update.effective_chat.id

    # 👮 Admin tekshiruvi
    member = await context.bot.get_chat_member(chat_id, user_id)
    is_admin = member.status in ["administrator", "creator"]

    # 🧠 Oddiy savol-javoblar
    if "necha yosh" in text:
        await update.message.reply_text("Men xozirda 22 yoshman, sizchi asalim😊")
        return
    elif "nima qilyapsan" in text or "nima gap" in text:
        await update.message.reply_text("bizda tinch ozindachi ybon 😊 mendan yordam kerakmasmi senga?")
        return
    elif "yoshin nechida" in text or "nechinchi yil" in text:
        await update.message.reply_text("Men xozirda 22 yoshman, sizchi asalim😊")
        return
    elif "seni sevaman" in text or "seni yaxshi koraman" in text:
        await update.message.reply_text("menham sizni ❤️ mendan boshqa sevganiz yoqmi")
        return
    elif "Assalomu alaykum" in text or "salom" in text:
        await update.message.reply_text("vaalaykum assalom")
        return
    elif "torimi" in text or "tog'rimi" in text:
        await update.message.reply_text("100% to'g'ri siz adashmesizu a")
        return
    elif "demagin" in text or "aytmagin" in text:
        await update.message.reply_text("xop boladi")
        return
    elif "sanga" in text or "senga" in text:
        await update.message.reply_text("raxmat")
        return
    elif "karta" in text or "card" in text:
        await update.message.reply_text("HAMKOR BANK\n"
                                           "👨🏽‍🦱MIRKOMILOV ASADBEK\n"
                                           "9860 1606 0295 0372")
        return
    elif "bomi ori" in text or "shaftoli" in text:
        await update.message.reply_text("qoto bor keremi")
        return
    elif "hayrli tun" in text or "dam oling" in text:
        await update.message.reply_text("sizham yaxshi dam oling, xayrli tun tushizda meni koring")
        return
    elif "pohhuy" in text or "pohuy" in text:
        await update.message.reply_text("pohuyda menga shunga yozdim")
        return
    elif "poxuy" in text or "poxuy" in text:
        await update.message.reply_text("pohuyda menga shunga yozdim")
        return
    elif "tabrik" in text or "heppy" in text:
        await update.message.reply_text("nima bilan")
        return
    elif "xotin" in text or "onasi" in text:
        await update.message.reply_text("qanday hali pampers yechmagan bosen turmediyamu")
        return
    elif "adasi" in text or "dada" in text:
        await update.message.reply_text("xo bolam gordaham tinch qoymagin meni")
        return
    elif "davay" in text or "kettik" in text:
        await update.message.reply_text("xoz shoshme turing")
        return
    elif "brat" in text or "bratim" in text:
        await update.message.reply_text("o' o' o' Assalomu alaykum bratim")
        return
    elif "juma" in text or "hayt" in text:
        await update.message.reply_text("raxmat sizgaham birga bolsin")
        return
    elif "seni sogindim" in text or "tezroq korishelik" in text:
        await update.message.reply_text("menham sizni ❤️ korishish muammomas joy bormi ishqilib")
        return
    elif "go 1vs1" in text or "go tdm" in text:
        await update.message.reply_text("siz zorsizu sizga yetadigoni yoq jonkam 😊")
        return
    elif "tdm" in text or "bot" in text:
        await update.message.reply_text("siz zorsizu sizga yetadigoni yoq jonkam 😊")
        return
    elif "qoto" in text or "кото" in text:
        await update.message.reply_text("siz hech qotoqga toymesiz ekanda a 🍆")
        return
    elif "qales" in text or "калиc" in text:
        await update.message.reply_text("yaxshi ozizchi nimalar qilyabsiz asalim ")
        return
    elif "🖕" in text or "🖕🏻" in text:
        await update.message.reply_text("shuni kotizga tiqib qoyamanda xozir ")
        return
    elif "kot" in text or "кот" in text:
        await update.message.reply_text("kotlama ushavolodinmi kot deysan")
        return
    elif "sexs" in text or "seks" in text:
        await update.message.reply_text("amini qis sexs korguncha")
        return
    elif "mani sevasanmi" in text or "meni sevasanmi" in text:
        await update.message.reply_text("burnini art oldin Asadbek akam turganda seni boshimga uramanmi")
        return
    elif "2x2=5" in text or "Hs q" in text:
        await update.message.reply_text("otni qotagi 5 e kallenga ske yban")
        return     
    elif "hala madrid" in text or "real madrid" in text:
        await update.message.reply_text("yban madrid 5;1 ga yutqizgan kot madrid")
        return
    elif "rostan" in text or "aniqmi" in text:
        await update.message.reply_text("xada ozim kordim")
        return
    elif "narx" in text or "qancha ekan" in text:
        await update.message.reply_text("sabr qiling, narxlar tez orada chiqadi")
        return
    elif "tez" in text or "Srochna" in text:
        await update.message.reply_text("shoshilma uka shoshilma e ana chichvording💩")
        return     
    elif "xaxa" in text or "😂" in text:
        await update.message.reply_text("kuloradikanda a ble hayt desa kuloradi")
        return      
    elif "seni kim yaratdi" in text or "kim yasadi" in text:
        await update.message.reply_text("Meni SLARK yaratgan 😊")
        return

  # So‘zlarni ajratish
    words = re.findall(r'\b\w+\b', text)

    # 1. So‘kinish tekshiruvi
    if not is_admin:
        if any(bad_word in text for bad_word in BAD_WORDS):
            await update.message.delete()
            user_warnings[user_id] = user_warnings.get(user_id, 0) + 1
            count = user_warnings[user_id]
            if count >= 3:
                await context.bot.restrict_chat_member(
                    chat_id=chat_id,
                    user_id=user_id,
                    permissions=ChatPermissions(can_send_messages=False),
                    until_date=int(time.time()) + 60
                )
                await context.bot.send_message(chat_id, f"⛔ @{update.message.from_user.username or 'Foydalanuvchi'} 3 marta ogohlantirildi. 1 daqiqaga bloklandi.")
            else:
                await context.bot.send_message(chat_id, f"⚠️ Ogohlantirish! So‘kinmang. ({count}/3)")
            return
    
    # Reklama
    if any(link_word in text for link_word in REKLAMA_SOZLAR):
        await update.message.delete()
        user_warnings[user_id] = user_warnings.get(user_id, 0) + 1
        count = user_warnings[user_id]

        if count >= 3:
                await context.bot.restrict_chat_member(
                    chat_id=chat_id,
                    user_id=user_id,
                    permissions=ChatPermissions(can_send_messages=False),
                    until_date=int(time.time()) + 60
                )
                await context.bot.send_message(chat_id, f"🚫 @{update.message.from_user.username or 'Foydalanuvchi'} reklama tarqatdi. 1 daqiqaga bloklandi.")
        else:
                await context.bot.send_message(chat_id, f"⚠️ Reklama taqiqlangan! ({count}/3)")
        return


# 2. Kalit so‘z havolalari
    for key in LINKS:
        if key in text:
            await update.message.reply_text(f"✅ Mana havola: {LINKS[key]}")
            return

# 3. Madina bilan suhbat
    if any(word in text for word in ["madina", "salom madina", "madish", "jonim", "asalim", "madishim"]):
        await update.message.reply_text("💬 Labbay jonim, sizga qanday yordam bera olaman? 😊")
        return

# 4. Tarjima faqat "madina" deb yozsa
    if "madi" in text:
        try:
            translated = GoogleTranslator(source='auto', target='uz').translate(text)
            if translated.lower() != text.lower():
                await update.message.reply_text(f"tarjima: {translated}")
                return
        except Exception as e:
            print(f"Tarjima xatosi: {e}")


        # --- Xatoliklarni tutuvchi funksiya ---
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"❗ Xatolik: {context.error}")

# === Botni ishga tushirish ===
if __name__ == '__main__':  
    app = ApplicationBuilder().token("7524826651:AAHAKkk24WT0AIVBFGQtY9K9scndNfZFBYQ").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, master_handler))

    app.post_init = on_start  # bot ishga tushganda eslatmani boshlaydi

    print("✅ Madina bot ishga tushdi...")
    app.run_polling()