import os
import threading
from flask import Flask
from pyrogram import Client, filters
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
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
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from datetime import datetime, time
import pytz



from datetime import datetime, time
import pytz

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    keyboard1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Check Result Now", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/8th/"))]
        ]
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/"))],
            [InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/"))],
            [InlineKeyboardButton("8th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/8th/"))]
        ]
    )

    if now.date() == datetime(2025, 5, 25, tzinfo=ist).date():
        if time(1, 0) <= now.time() < time(10, 0):
            await message.reply_text(
                "**आज कक्षा 8 का परिणाम जारी किया जायेगा!**\n"
                "परिणाम शाम **5 बजे तक** आएगा। कृपया रोल नंबर तैयार रखें।\n\n"
                "**Class 8th result will be declared today by 5 PM.**\n"
                "Please keep your roll number ready.",
                reply_markup=keyboard1
            )

        elif time(10, 0) <= now.time() < time(13, 0):
            await message.reply_text(
                "**कक्षा 8 का परिणाम दोपहर बाद जारी किया जाएगा।**\n"
                "शाम **5 बजे तक** परिणाम आने की संभावना है। कृपया प्रतीक्षा करें।\n\n"
                "**Class 8th result will be released post noon.**\n"
                "Expected by 5:00 PM. Please stay tuned.",
                reply_markup=keyboard1
            )

        elif time(13, 0) <= now.time() < time(16, 0):
            await message.reply_text(
                "**कक्षा 8 का परिणाम जल्द ही जारी किया जाएगा!**\n"
                "शाम **5 बजे** तक परिणाम देखने के लिए तैयार रहें।\n\n"
                "**Class 8th result is coming soon!**\n"
                "Be ready to check it by 5:00 PM.",
                reply_markup=keyboard1
            )

        elif time(16, 0) <= now.time() < time(16, 30):
            await message.reply_text(
                "**कक्षा 8 का रिजल्ट कुछ ही देर में जारी किया जाएगा...**\n"
                "कृपया इंतजार करें और बार-बार चेक न करें।\n\n"
                "**Class 8th result is about to go live.**\n"
                "Please wait patiently and avoid refreshing repeatedly.",
                reply_markup=keyboard1
            )

        elif time(16, 30) <= now.time() <= time(18, 0):
            await message.reply_text(
                "**कक्षा 8 का परिणाम अब जारी कर दिया गया है!**\n"
                "नीचे दिए गए विकल्प से अपना रोल नंबर डालकर तुरंत रिजल्ट देखें।\n\n"
                "**Class 8th result is now live!**\n"
                "Enter your roll number below to view it instantly.",
                reply_markup=keyboard1
            )
    elif now.date() == datetime(2025, 5, 24, tzinfo=ist).date():
        await message.reply_text(
                "**कल कक्षा 8 का परिणाम जारी किया जायेगा!**\n"
                "परिणाम शाम **5 बजे तक** आएगा। कृपया रोल नंबर तैयार रखें।\n\n"
                "**Class 8th result will be declared tomorrow by 5 PM.**\n"
                "Please keep your roll number ready.",
                reply_markup=keyboard1
        )
    await message.reply_text(
            "Welcome to **SingodiyaTech Result Bot!**\n\n"
            "Check your Rajasthan Board Result for 10th, 12th, and 8th in one click.\n\n"
            "**Steps:**\n"
            "1. Tap the button below\n"
            "2. Enter your roll number\n"
            "3. Get your marks instantly as PDF or online view.\n\n"
            "Use /help command to get help.\n"
            "If current server getting failed, please use /Server2 command.",
            reply_markup=keyboard
        )
        
@app.on_message(filters.command(["NAMEWISE", "NameWise" , "Namewise","namewise"]) & filters.private)
async def start_handler(client, message):
    text = """
Welcome to **SingodiyaTech Result Bot!**\n\n            
Check your Rajasthan Board Result for 10th & 12th in one click by name.\n\n
**NAMEWISE RESULT 2025**

**Steps:**
1. Tap the button below
2. Enter your Name
3. Confirm your Name and Fathers Name.
4. Click on get.
             
**Use /help command to get help.**
"""

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    "10th Result 2025",
                    web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/NameWise/")
                )
            ],
            [
                InlineKeyboardButton(
                    "12th Result 2025",
                    web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/NameWise")
                )
            ]
        ]
    )

    await message.reply_text(
        text,
        reply_markup=keyboard
    )

@app.on_message(filters.command(["help", "Help"]) & filters.private )
async def help_handler(client, message):
    await message.reply_text(
        "**Help Guide**\n\n"
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
        "• **Still need help? Contact our support @aks979.**"
    )
@app.on_message(filters.command(["About", "about"]) & filters.private )
async def about_handler(client, message):
    await message.reply_text(
        "About This Bot\n\n"
        "This bot helps students access their results and exam info quickly.\n"
        "**Maintained by:** @Aks979\n"
        "**Powered by**: SingodiyaTech"
    )


@app.on_message(filters.command(["result2025", "Result2025"]) & filters.private)
async def old_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th RollWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/")),
            InlineKeyboardButton("10th NameWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/NameWise"))
        ],
        [
            InlineKeyboardButton("12th RollWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/")),
            InlineKeyboardButton("12th NameWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/NameWise"))
        ],
        [
                InlineKeyboardButton(
                    "8th Result 2025",
                    web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/8th/")
                )
            ]
    ])
    
    await message.reply_text(
        "Chack Your Result for 2025.\n** Select a Button Below**\n\nEach button will open a web app for that specific Class.",
        reply_markup=keyboard
    )
@app.on_message(filters.command(["OldResult", "old_result"]) & filters.private)
async def old_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("2024 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2024/10th/")),
            InlineKeyboardButton("2024 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2024/12th/"))
        ],
        [
            InlineKeyboardButton("2023 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2023/10th/")),
            InlineKeyboardButton("2023 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2023/12th/"))
        ],
        [
            InlineKeyboardButton("2022 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2022/10th/")),
            InlineKeyboardButton("2022 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2022/12th/"))
        ]
    ])
    
    await message.reply_text(
        "Previous Year Results\n\n"
        "Select year below to check 10th or 12th result:\n"
        "Each button will open a web app for that specific year.",
        reply_markup=keyboard
    )
@app.on_message(filters.command(["OldResultNamewise", "old_result_namewise"]) & filters.private)
async def old_result_handler(client, message):
    text = """
"**Previous Year Results (Name Wise)**
Select year below to check 10th or 12th result:
Each button will open a web app for that specific year (Name Wise).
"""
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("2024 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2024/10th/NameWise/")),
            InlineKeyboardButton("2024 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2024/12th/NameWise/"))
        ],
        [
            InlineKeyboardButton("2023 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2023/10th/NameWise/")),
            InlineKeyboardButton("2023 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2023/12th/NameWise/"))
        ],
        [
            InlineKeyboardButton("2022 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2022/10th/NameWise/")),
            InlineKeyboardButton("2022 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2022/12th/NameWise/"))
        ]
    ])
    
    await message.reply_text(text,
        reply_markup=keyboard
    )
@app.on_message(filters.command(["Feedback", "feedback"]) & filters.private )
async def feedback_handler(client, message):
    feedback_msg = (
        "Feedback & Suggestions\n\n"
        "We value your opinion!\n"
        "• Send your feedback here: [SingodiyaTeck](t.me/mr_singodiyabot)\n"
        "• Or email us at: raindropgbstar@gmail.com"
    )
    await message.reply_text(feedback_msg)

@app.on_message(filters.command(["ContactAdmin", "contact_admin"]) & filters.private)
async def contact_admin_handler(client, message):
    admin_msg = (
        "Contact Admin\n\n"
        "• Mention your issue clearly.\n"
        "• Admin: @aks979\n"
        "• Support hours: 10 AM to 10 PM (Mon–Sun)"
    )
    await message.reply_text(admin_msg)

@app.on_message(filters.command(["SchoolWise", "school_wise"]) & filters.private)
async def school_wise_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/SchoolWise"))
        ],
        [
            InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/SchoolWise"))
        ]
    ])

    text = (
        "Welcome to Rajasthan Result Bot!\n\n"
        "Check your Rajasthan Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your School's First Student Roll Number and Last Student Roll Number\n"
        "3. Get your Full School Table!\n"
        "Use /help command to see more commands."
    )

    await message.reply_text(text, reply_markup=keyboard)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(filters.command(["Server2", "server2"]) & filters.private)
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/Server2"))
        ],
        [
            InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/Server2"))
        ]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 2 \n\n**"
        "Check your Rajasthan Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /help command to get help."
    )

    await message.reply_text(text, reply_markup=keyboard)
@app.on_message(filters.command(["Server3", "Server3"]) & filters.private)
async def server3_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/Server3"))
        ],
        [
            InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/Server3"))
        ]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 3 \n\n**"
        "Check your Rajasthan Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /help command to get help."
    )

    await message.reply_text(text, reply_markup=keyboard)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    run_bot()
