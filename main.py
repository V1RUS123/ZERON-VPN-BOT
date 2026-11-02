import os
import telebot
from telebot import types

TOKEN = os.getenv("TOKEN_BOTA_TELEGRAM")

if not TOKEN:
    raise RuntimeError("Токен бота не налаштовано!")

bot = telebot.TeleBot(TOKEN)

def menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🌐 Підключити VPN", "🌍 Країни")
    kb.row("👤 Профіль", "📊 Статус")
    kb.row("❓ Допомога")
    return kb

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🛡 ZERON VPN\n\n"
        "Вітаємо в ZERON VPN!\n"
        "Вибери потрібну функцію 👇",
        reply_markup=menu()
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "🛡 ZERON VPN — Допомога\n\n"
        "/start — головне меню\n"
        "/help — допомога\n"
        "/status — статус сервісу"
    )

@bot.message_handler(commands=["status"])
def status(message):
    bot.send_message(
        message.chat.id,
        "🟢 Telegram-бот працює.\n"
        "🔴 VPN-сервер ще не підключений."
    )

@bot.message_handler(content_types=["text"])
def messages(message):
    text = message.text

    if text == "🌐 Підключити VPN":
        reply = "🔴 VPN поки недоступний. Налаштовуємо сервер."

    elif text == "🌍 Країни":
        reply = "🌍 Доступних серверів поки немає."

    elif text == "👤 Профіль":
        reply = (
            f"👤 Ім'я: {message.from_user.first_name}\n"
            f"🆔 ID: {message.from_user.id}"
        )

    elif text == "📊 Статус":
        reply = "🟢 Бот активний.\n🔴 VPN ще не налаштовано."

    elif text == "❓ Допомога":
        reply = "🛡 ZERON VPN\nВикористовуй кнопки меню."

    else:
        reply = "Вибери кнопку з меню 👇"

    bot.send_message(message.chat.id, reply, reply_markup=menu())

print("ZERON VPN Bot запущено!")
bot.infinity_polling(skip_pending=True)
