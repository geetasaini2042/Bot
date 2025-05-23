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
        reply_markup=keyboard
    )
@app.on_message(filters.command(["help", "Help"]) & filters.private & filters.user(lambda _, __, msg: not msg.from_user.is_bot))
async def help_handler(client, message):
    await message.reply_text(
        "Help Guide\n\n"
        "• Use 10th or 12th buttons to open result web apps.\n"
        "• Use /NameWise to get your result by Name.\n"
        "• Use /SchoolWise to get all school result in one table.\n"
        "• Use /result2025 to get 2025 results\n"
        "• Use /Server2 if the current server is not working\n"
        "• Use /OldResult command to get Previous Years Results.\n"
        "• Use /oldResultNamewise command to get Previous Years Results By Name.\n"
        "• Use /About for revaluation or rechecking details.\n"
        "• Use /Feedback to leave a feedback about Bot\n"
        "• Use /ContactAdmin to see all support options available.\n\n"
        "• Still need help? Contact our support @aks979."
    )
@app.on_message(filters.command(["About", "about"]) & filters.private & filters.user(lambda _, __, msg: not msg.from_user.is_bot))
async def about_handler(client, message):
    await message.reply_text(
        "About This Bot\n\n"
        "This bot helps students access their results and exam info quickly.\n"
        "Maintained by: @Aks979\n"
        "Powered by: SingodiyaTech"
    )

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(filters.command(["OldResult", "old_result"]) & filters.private & filters.user(lambda _, __, msg: not msg.from_user.is_bot))
async def old_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("2024 - 10th", web_app={"url": "https://geetasaini2042.github.io/Results/RAJ/2024/10th/"}),
            InlineKeyboardButton("2024 - 12th", web_app={"url": "https://geetasaini2042.github.io/Results/RAJ/2024/12th/"})
        ],
        [
            InlineKeyboardButton("2023 - 10th", web_app={"url": "https://geetasaini2042.github.io/Results/RAJ/2023/10th/"}),
            InlineKeyboardButton("2023 - 12th", web_app={"url": "https://geetasaini2042.github.io/Results/RAJ/2023/12th/"})
        ],
        [
            InlineKeyboardButton("2022 - 10th", web_app={"url": "https://geetasaini2042.github.io/Results/RAJ/2022/10th/"}),
            InlineKeyboardButton("2022 - 12th", web_app={"url": "https://geetasaini2042.github.io/Results/RAJ/2022/12th/"})
        ]
    ])
    
    await message.reply_text(
        "Previous Year Results\n\n"
        "Select year below to check 10th or 12th result:\n"
        "Each button will open a web app for that specific year.",
        reply_markup=keyboard
    )
# Entry point
if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    run_bot()
