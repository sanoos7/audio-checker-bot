import telebot

BOT_TOKEN = "8557808707:AAE9AXJELXwjURuU3RM03C99QyC2qpOsXA4"

bot = telebot.TeleBot(BOT_TOKEN)

# ✅ Start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🎧 Send me an audio file to check Lossless or Lossy")

# ✅ Handle audio/files
@bot.message_handler(content_types=['audio', 'document'])
def handle_audio(message):
    bot.reply_to(message, "📥 File received!\n🔍 Analysis coming soon...")

# ✅ Run bot (NO webhook)
print("Bot running...")
bot.infinity_polling()@app.route("/", methods=["POST"])
def webhook():
    data = request.json

    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")

    # ✅ Handle /start
    if "text" in message:
        if message["text"] == "/start":
            requests.post(
                f"https://api.telegram.org/bot{8557808707:AAE9AXJELXwjURuU3RM03C99QyC2qpOsXA4}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": "🎧 Send me an audio file to check if it's Lossless or Lossy"
                }
            )
            return "ok"
