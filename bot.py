import os
import threading
from flask import Flask
from pyrogram import Client, filters
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials from environment
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create Flask app
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Flask server is running."

# Define run_flask function
def run_flask():
    flask_app.run(host="0.0.0.0", port=5000)

# Create Pyrogram Client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define run_bot function
def run_bot():
    app.run()

# Pyrogram handler

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    text = (
        "Welcome to *SingodiyaTech Result Bot!*\n\n"
        "Check your Rajasthan Board Result for 10th & 12th in one click.\n\n"
        "*Steps:*\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /help command to get help.\n"
        "If current server getting failed. Please use /Server2 Command."
    )

    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "10th Result 2025",
                    "web_app": {"url": "https://geetasaini2042.github.io/Results/RAJ/2025/10th/"}
                }
            ],
            [
                {
                    "text": "12th Result 2025",
                    "web_app": {"url": "https://geetasaini2042.github.io/Results/RAJ/2025/12th/"}
                }
            ]
        ]
    }

    await message.reply_text(
        text,
        parse_mode="markdown",
        reply_markup=keyboard
    )
# Entry point
if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    run_bot()
