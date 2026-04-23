@app.route("/", methods=["POST"])
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
