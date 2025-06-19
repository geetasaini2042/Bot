# bot.py
from script import app, run_flask, run_bot
import threading
from pyrogram import Client, filters
from datetime import datetime, time
import pytz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import rajasthan , uttarpradesh, andhrapradesh

year = "2025"
ADMINS = [6150091802]
home_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Rajasthan Results",callback_data="rj_board_results")
            ],   
                        [
                InlineKeyboardButton("UP Board Results",callback_data="up_board_result")
            ],
                        [
                InlineKeyboardButton("AP Board Results",callback_data="ap_board_result")
            ]


        ]
    )
board_keyboard = InlineKeyboardMarkup([
    [  # Rajasthan row
        InlineKeyboardButton(
            "Raj 10th",
            web_app=WebAppInfo(
                url=f"https://geetasaini2042.github.io/Results/RAJ/{year}/10th/"
            )
        ),
        InlineKeyboardButton(
            "Raj 12th",
            web_app=WebAppInfo(
                url=f"https://geetasaini2042.github.io/Results/RAJ/{year}/12th/"
            )
        ),
        InlineKeyboardButton(
            "...",
            callback_data="rj_board_result"
        )
    ],
    [  # UP row
        InlineKeyboardButton(
            "UP 10th",
            web_app=WebAppInfo(
                url=f"https://geetasaini2042.github.io/Results/UP/{year}/10th/"
            )
        ),
        InlineKeyboardButton(
            "UP 12th",
            web_app=WebAppInfo(
                url=f"https://geetasaini2042.github.io/Results/UP/{year}/12th/"
            )
        ),
        InlineKeyboardButton(
            "...",
            callback_data="up_board_result"
        )
    ],
    [  # AP row
        InlineKeyboardButton(
            "AP 10th",
            web_app=WebAppInfo(
                url=f"https://geetasaini2042.github.io/Results/AP/{year}/10th/"
            )
        ),
        InlineKeyboardButton(
            "AP 11th",
            web_app=WebAppInfo(
                url=f"https://geetasaini2042.github.io/Results/AP/{year}/11th/"
            )
        ),
        InlineKeyboardButton(
            "...",
            callback_data="ap_board_result"
        )
    ]
])
@app.on_message(filters.private & filters.command("start") & filters.regex(r"^/start$"))
async def start_handler(client, message):
  await message.reply_text(
            "Welcome to **SingodiyaTech Result Bot!**\n\n"
            "Check your Board Exam Results in one click.\n\n"
            "**Steps:**\n"
            "1. Choose Your Board below\n"
            "2. Select Your Class."
            "3. Get your marks instantly as PDF or online view.\n\n"
            "Use help command to get help.\n",
            reply_markup=home_keyboard
        )
@app.on_callback_query(filters.regex("^start$"))
async def start_handler(client, callback_query):
  await callback_query.message.edit_text(
            "Welcome to **SingodiyaTech Result Bot!**\n\n"
            "Check your Exam Results in one click.\n\n"
            "**Steps:**\n"
            "1. Choose Your Exam below\n"
            "2. Select Your Board, University or Other Exam"
            "3. Get your marks instantly as PDF or online view.\n\n"
            "Use help command to get help.\n",
            reply_markup=home_keyboard
        )
board_result_msg = (
            "Welcome to **SingodiyaTech Result Bot!**\n\n"
            "Check your state Board Result for 10th, 12th, 8th and 5th in one click.\n\n"
            "**Steps:**\n"
            "1. Choose your State and Class below\n"
            "2. Enter your roll number\n"
            "3. Get your marks instantly as PDF or online view.\n\n"
            "Use /board_help command to get help.\n")

@app.on_message(filters.command(["board_exams", "school_boards"]) & filters.private)
async def msg_handler(client, message):
    await message.reply_text(board_result_msg,reply_markup=board_keyboard)
@app.on_callback_query(filters.regex("^boards_results$"))
async def board_result_query_handler(client, callback_query):
  await callback_query.message.edit_text(board_result_msg,reply_markup=board_keyboard)
  
  
@app.on_message(filters.command(["help", "HELP", "board_help"]) & filters.private)
async def msg_handler(client, message):
    msg = (
            "Welcome to **SingodiyaTech Result Bot!**\n\n"
            "Check your State Board Result for 10th, 12th, 8th and 5th in one click.\n\n"
            "**Steps:**\n"
            "1. Choose your State and Class below\n"
            "2. Enter your roll number\n"
            "3. Get your marks instantly as PDF or online view.\n\n"
            "Use /board_help command to get help.\n"
            "If current server getting failed, please Use /Server2 command.")
    await message.reply_text(msg)
@app.on_message(filters.command(["ContactAdmin", "contact_admin"]) & filters.private)
async def contact_admin_handler(client, message):
    admin_msg = (
        "Contact Admin\n\n"
        "• Mention your issue clearly.\n"
        "• Admin: @aks979\n"
        "• Support hours: 10 AM to 10 PM (Mon–Sun)"
    )
    await message.reply_text(admin_msg)

@app.on_message(filters.command(["Feedback", "feedback"]) & filters.private )
async def feedback_handler(client, message):
    feedback_msg = (
        "Feedback & Suggestions\n\n"
        "We value your opinion!\n"
        "• Send your feedback here: [SingodiyaTeck](t.me/mr_singodiyabot)\n"
        "• Or email us at: raindropgbstar@gmail.com"
    )
    await message.reply_text(feedback_msg)

new_year = 2025
        
@app.on_message(filters.command(["NAMEWISE", "NameWise" , "Namewise", "namewise"]) & filters.private)
async def startname_handler(client, message):
    text = """
Welcome to **SingodiyaTech Result Bot!**\n\n            
Check your Board Result in one click by name.\n\n
**NAMEWISE RESULT 2025**

**Steps:**
1. Tap the button below
2. Enter your Name
3. Confirm your Name and Fathers Name.
4. Click on get.
             
**Use /help command to get help.**
"""

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("RBSE Board", callback_data="rj_namewise")
        ],
        [
            InlineKeyboardButton("UPMSP BOARD", callback_data="up_namewise")
        ],
        [InlineKeyboardButton("BSEAP BOARD", callback_data="ap_namewise")]
    ])

    await message.reply_text(
        text,
        reply_markup=keyboard
    )
@app.on_callback_query(filters.regex("^namewise$"))
async def startname_handler(client, message):
    text = """
Welcome to **SingodiyaTech Result Bot!**\n\n            
Check your Board Result in one click by name.\n\n
**NAMEWISE RESULT 2025**

**Steps:**
1. Tap the button below
2. Enter your Name
3. Confirm your Name and Fathers Name.
4. Click on get.
             
**Use /help command to get help.**
"""

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("RBSE Board", callback_data="rj_namewise")
        ],
        [
            InlineKeyboardButton("UPMSP BOARD", callback_data="up_namewise")
        ],
        [InlineKeyboardButton("BSEAP BOARD", callback_data="ap_namewise")]
    ])

    await message.message.edit_text(
        text,
        reply_markup=keyboard
    )


@app.on_message(filters.command(["result2025", "Result2025"]) & filters.private)
async def new_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("RBSE Board", callback_data="rj_result2025")
        ],
        [
            InlineKeyboardButton("UPMSP BOARD", callback_data="up_result2025")
        ],
        [InlineKeyboardButton("BSEAP BOARD", callback_data="ap_result2025")]
    ])
    
    await message.reply_text(
        "Chack Your Result for 2025.\n** Select a Button Below**\n\nEach button will open a web app for that specific Class.",
        reply_markup=board_keyboard
    )
@app.on_message(filters.command(["OldResult", "old_result"]) & filters.private)
async def old_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("RBSE Board", callback_data="rj_old")
        ],
        [
            InlineKeyboardButton("UPMSP BOARD", callback_data="up_old")
        ],
        [InlineKeyboardButton("BSEAP BOARD", callback_data="ap_old")]
    ])
    
    await message.reply_text(
        "Previous Year Results\n\n"
        "Select year below to check 10th or 12th result:\n"
        "Each button will open a web app for that specific year.",
        reply_markup=keyboard
    )
@app.on_callback_query(filters.regex("^old$"))
async def old_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("RBSE Board", callback_data="rj_old")
        ],
        [
            InlineKeyboardButton("UPMSP BOARD", callback_data="up_old")
        ],
        [InlineKeyboardButton("BSEAP BOARD", callback_data="ap_old")]
    ])
    
    await message.message.edit_text(
        "Previous Year Results\n\n"
        "Select year below to check 10th or 12th result:\n"
        "Each button will open a web app for that specific year.",
        reply_markup=keyboard
    )
@app.on_message(filters.command(["OldResultNamewise", "old_result_namewise"]) & filters.private)
async def old_result_handler(client, message):
    text = """
"**Previous Year Results (Name Wise)**
Select Board below to check 10th or 12th result:
Each button will open that specific(Name Wise).
"""
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("RBSE Board", callback_data="rj_oldname")
        ],
        [
            InlineKeyboardButton("UPMSP BOARD", callback_data="up_oldname")
        ],
        [InlineKeyboardButton("BSEAP BOARD", callback_data="ap_oldname")]
    ])
    await message.reply_text(text,
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("^oldname$"))
async def old_result_handler(client, message):
    text = """
"**Previous Year Results (Name Wise)**
Select Board below to check 10th or 12th result:
Each button will open that specific(Name Wise).
"""
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("RBSE Board", callback_data="rj_oldname")
        ],
        [
            InlineKeyboardButton("UPMSP BOARD", callback_data="up_oldname")
        ],
        [InlineKeyboardButton("BSEAP BOARD", callback_data="ap_oldname")]
    ])
    await message.message.edit_text(text,
        reply_markup=keyboard
    )
@app.on_message(filters.command(["SchoolWise", "school_wise"]) & filters.private)
async def school_wise_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Rajasthan Board", callback_data="rj_schoolwise")
        ]
    ])

    text = (
        "Welcome to Result Bot!\n\n"
        "Check your Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your School's First Student Roll Number and Last Student Roll Number\n"
        "3. Get your Full School Table!\n"
        "Use /help command to see more commands."
    )

    await message.reply_text(text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^schoolwise$"))
async def school_wise_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Rajasthan Board", callback_data="rj_schoolwise")
        ]
    ])

    text = (
        "Welcome to Result Bot!\n\n"
        "Check your Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your School's First Student Roll Number and Last Student Roll Number\n"
        "3. Get your Full School Table!\n"
        "Use /help command to see more commands."
    )

    await message.message.edit_text(text, reply_markup=keyboard)

@app.on_message(filters.command(["Server2", "server2"]) & filters.private)
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("RBSE Board", callback_data="rj_server2")
        ],
        [
            InlineKeyboardButton("UPMSP BOARD", callback_data="up_server2")
        ],
        [InlineKeyboardButton("BSEAP BOARD", callback_data="ap_server2")]
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
@app.on_callback_query(filters.regex("^server2$"))
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("RBSE Board", callback_data="rj_server2")
        ],
        [
            InlineKeyboardButton("UPMSP BOARD", callback_data="up_server2")
        ],
        [InlineKeyboardButton("BSEAP BOARD", callback_data="ap_server2")]
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

    await message.message.edit_text(text, reply_markup=keyboard)
@app.on_message(filters.command(["Server3", "Server3"]) & filters.private)
async def server3_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Rajasthan Board", callback_data="rj_server3")
        ]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 3 \n\n**"
        "Check your Board Results for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Select the Board and class below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /help command to get help."
    )

    await message.reply_text(text, reply_markup=keyboard)
@app.on_callback_query(filters.regex("^server3$"))
async def server3_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Rajasthan Board", callback_data="rj_server3")
        ]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 3 \n\n**"
        "Check your Board Results for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Select the Board and class below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /help command to get help."
    )

    await message.message.edit_text(text, reply_markup=keyboard)
@app.on_message(filters.command(["commands", "available_commands"]) & filters.private)
async def server3_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Next ⏭️", callback_data="rj_commands")
        ]
    ])

    text = """
📋 **Available Bot Commands**

🔰 **Main Commands**
• /start - Start the bot and see main options
• /help - Rajasthan Board Help & Usage Guide
• /available_commands - Show all available commands (this list)

🏫 **School/Board Results**
• /board_exams or /school_boards - View state board results (Raj/UP/AP)
• /competition_exams - View Other Exam Results (NEET/JEE/NDA/UPSC..)
• /university_results - View University Results
• /board_help - Help for school board results
• /result2025 - Latest 2025 Board Results
• /OldResult - Previous year results
• /OldResultNamewise - Name-wise old results

🔍 **Result Search Options**
• /NameWise - Search result by student name
• /SchoolWise - Get all results for a school
• /Server2, /Server3 - Alternate result servers

📩 **Feedback & Support**
• /Feedback - Send your feedback or suggestion
• /ContactAdmin - Get contact details of support admin
"""

    await message.reply_text(text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^commands$"))
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Next ⏭️", callback_data="rj_commands")
        ]
    ])

    text = """
📋 **Available Bot Commands**

🔰 **Main Commands**
• /start - Start the bot and see main options
• /help - Rajasthan Board Help & Usage Guide
• /available_commands - Show all available commands (this list)

🏫 **School/Board Results**
• /board_exams or /school_boards - View state board results (Raj/UP/AP)
• /competition_exams - View Other Exam Results (NEET/JEE/NDA/UPSC..)
• /university_results - View University Results
• /board_help - Help for school board results
• /result2025 - Latest 2025 Board Results
• /OldResult - Previous year results
• /OldResultNamewise - Name-wise old results

🔍 **Result Search Options**
• /NameWise - Search result by student name
• /SchoolWise - Get all results for a school
• /Server2, /Server3 - Alternate result servers

📩 **Feedback & Support**
• /Feedback - Send your feedback or suggestion
• /ContactAdmin - Get contact details of support admin
"""

    await message.message.edit_text(text, reply_markup=keyboard)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    run_bot()
