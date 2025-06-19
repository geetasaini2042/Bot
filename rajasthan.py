#    rajasthan.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from datetime import datetime, time
import pytz
from script import app
new_year = 2025

@app.on_message( filters.private & (
        filters.command("rj_start") |
        (filters.command("start") & filters.regex(r"^/start(@\w+)?\s+rj_board_result$"))
    )
)
async def start_handler(client, message):
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    keyboard1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Check Result Now", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/5th/"))]
        ]
    )
    keyboard2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("5th Server 1", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/5th/"))],
            [InlineKeyboardButton("5th Server 2", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/5th/Server2"))]
            
        
        ]
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/"))],
            [InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/"))],
            [InlineKeyboardButton("8th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/8th/Server2"))],
            [InlineKeyboardButton("5th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/5th/Server2"))]

        ]
    )
    await message.reply_text(
            "Welcome to **SingodiyaTech Result Bot!**\n\n"
            "Check your Rajasthan Board Result for 10th, 12th, 8th and 5th in one click.\n\n"
            "**Steps:**\n"
            "1. Tap the button below\n"
            "2. Enter your roll number\n"
            "3. Get your marks instantly as PDF or online view.\n\n"
            "Use /rj_help command to get help.\n"
            "If current server getting failed, please Use /rj_Server2 command.",
            reply_markup=keyboard
        )

    if now.date() == datetime(2025, 5, 30, tzinfo=ist).date():
        if time(1, 0) <= now.time() < time(8, 0):
            await message.reply_text(
                "**आज कक्षा 5 का परिणाम जारी किया जायेगा!**\n\n"
                "परिणाम दोपहर **12:30 बजे तक** आएगा। विद्यार्थी अपने Roll Number से अपना Result निकाल सकते हैं।\n\n"
                "**Class 5th result will be declared today by 12:30 PM.**\n"
                "Please keep your roll number ready.",
                reply_markup=keyboard1
            )

        elif time(8, 0) <= now.time() < time(10, 30):
            await message.reply_text(
                "**कक्षा 5 का परिणाम दोपहर बाद जारी किया जाएगा।**\n"
                "दोपहर **12:30 बजे तक** परिणाम आएगा कृपया प्रतीक्षा करें...\n\n"
                "**Class 5th result will be released post noon.**\n"
                "Expected by 12:30 PM. Please stay tuned.",
                reply_markup=keyboard1
            )

        elif time(10, 30) <= now.time() < time(11, 45):
            await message.reply_text(
                "**कक्षा 5 का परिणाम जल्द ही जारी किया जाएगा!**\n"
                "दोपहर **12:30 बजे** तक परिणाम देखने के लिए तैयार रहें।\n\n"
                "**Class 5th result is coming soon!**\n"
                "Be ready to check it by 12:30 PM.",
                reply_markup=keyboard1
            )

        elif time(11, 45) <= now.time() < time(12,40):
            await message.reply_text(
                "**कक्षा 5 का रिजल्ट कुछ ही देर में जारी किया जाएगा...**\n"
                "कृपया इंतजार करें..\n\n"
                "**Please Wait...**\n\n"
                "**Class 5th result is about to go live.**\n"
                "Please wait patiently and avoid refreshing repeatedly.",
                reply_markup=keyboard2
            )

        elif time(12, 40) <= now.time() <= time(22, 0):
            await message.reply_text(
                "**कक्षा 5 का परिणाम अब जारी कर दिया गया है!**\n"
                "नीचे दिए गए विकल्प से अपना रोल नंबर डालकर तुरंत रिजल्ट देखें।\n\n"                
                "**Class 5th result is now live!**\n"
                "Enter your roll number below to view it instantly.\n\n",
                reply_markup=keyboard2
            )
    elif now.date() == datetime(2025, 5, 29, tzinfo=ist).date():
        await message.reply_text(
                "**कल कक्षा 5 का परिणाम जारी किया जायेगा!**\n\n"
                "परिणाम दोपहर **12:30 बजे तक** आएगा। विद्यार्थी अपने Roll Number से अपना Result निकाल सकते हैं।\n\n"
                "**Class 5th result will be declared tomorrow by 12:30 PM.**\n"
                "Please keep your roll number ready.",
                reply_markup=keyboard1
        )
        
@app.on_message(filters.command(["rj_NAMEWISE", "rj_NameWise" , "rj_Namewise", "rj_namewise"]) & filters.private)
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
             
**Use /rj_help command to get help.**
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

@app.on_callback_query(filters.regex("^rj_namewise$"))
async def start_handler_query(client, callback_query):
    text = """
Welcome to **SingodiyaTech Result Bot!**\n\n            
Check your Rajasthan Board Result for 10th & 12th in one click by name.\n\n
**NAMEWISE RESULT 2025**

**Steps:**
1. Tap the button below
2. Enter your Name
3. Confirm your Name and Fathers Name.
4. Click on get.
             
**Use /rj_help command to get help.**
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
            ],
               [
          InlineKeyboardButton("🔙Back",callback_data="namewise")
        ]
        ]
    )

    await callback_query.message.edit_text(
        text,
        reply_markup=keyboard
    )

@app.on_message(filters.command(["rj_help", "rj_Help"]) & filters.private )
async def help_handler(client, message):
    await message.reply_text(
        "**Help Guide For Rajasthan Board**\n\n"
        "• Use 10th or 12th buttons to open result web apps.\n"
        "• Use /rj_NameWise to get your result by Name.\n"
        "• Use /rj_SchoolWise to get all school result in one table.\n"
        "• Use /rj_result2025 to get 2025 results\n"
        "• Use /rj_Server2 if the current server is not working\n"
        "• Use /rj_OldResult command to get Previous Years Results.\n"
        "• Use /rj_oldResultNamewise command to get Previous Years Results By Name.\n"
        "• Use /rj_About for revaluation or rechecking details.\n"
        "• Use /rj_Feedback to leave a feedback about Bot\n"
        "• Use /rj_ContactAdmin to see all support options available.\n\n"
        "• **Still need help? Contact our support @aks979.**"
    )

@app.on_message(filters.command(["rj_result2025", "rj_Result2025"]) & filters.private)
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
            InlineKeyboardButton("8th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/8th/Server2"))
        ],
        [ 
            InlineKeyboardButton("5th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/5th/Server2"))
        ]

    ])
    
    await message.reply_text(
        "Chack Your Result for 2025.\n** Select a Button Below**\n\nEach button will open a web app for that specific Class.",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("^rj_result2025$"))
async def old_result_handler_query(client, callback_query):
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
            InlineKeyboardButton("8th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/8th/Server2"))
        ],
        [ 
            InlineKeyboardButton("5th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/5th/Server2"))
        ],
         [
          InlineKeyboardButton("🔙Back",callback_data="start")
        ]

    ])
    
    await callback_query.message.edot_text(
        "Chack Your Result for 2025.\n** Select a Button Below**\n\nEach button will open a web app for that specific Class.",
        reply_markup=keyboard
    )
@app.on_message(filters.command(["rj_OldResult", "rj_old_result"]) & filters.private)
async def old_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("2025 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/")),
            InlineKeyboardButton("2025 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/"))
        ],
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
        reply_markup=keyboard)
    
@app.on_callback_query(filters.regex("^rj_old$"))
async def old_result_handler_query(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("2025 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/")),
            InlineKeyboardButton("2025 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/"))
        ],
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
    
    await callback_query.message.edit_text(
        "Previous Year Results\n\n"
        "Select year below to check 10th or 12th result:\n"
        "Each button will open a web app for that specific year.",
        reply_markup=keyboard
    )
@app.on_message(filters.command(["rj_OldResultNamewise", "rj_old_result_namewise"]) & filters.private)
async def old_result_handler(client, message):
    text = """
"**Previous Year Results (Name Wise)**
Select year below to check 10th or 12th result:
Each button will open a web app for that specific year (Name Wise).
"""
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("2025 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/NameWise/")),
            InlineKeyboardButton("2025 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/NameWise/"))
        ],
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
        ],
         [
          InlineKeyboardButton("🔙Back",callback_data="old")
        ]
    ])
    
    await message.reply_text(text,
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("^rj_oldname$"))
async def old_result_handler_query(client, callback_query):
    text = """
"**Previous Year Results (Name Wise)**
Select year below to check 10th or 12th result:
Each button will open a web app for that specific year (Name Wise).
"""
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("2025 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/NameWise/")),
            InlineKeyboardButton("2025 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/NameWise/"))
        ],
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
    
    await callback_query.message.edit_text(text,
        reply_markup=keyboard
    )


@app.on_message(filters.command(["rj_SchoolWise", "rj_school_wise"]) & filters.private)
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
        "Use /rj_help command to see more commands."
    )

    await message.reply_text(text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^rj_schoolwise$"))
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
        "Use /rj_help command to see more commands."
    )

    await message.reply_text(text, reply_markup=keyboard)

@app.on_message(filters.command(["rj_Server2", "rj_server2"]) & filters.private)
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/Server2"))
        ],
        [
            InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/Server2"))
        ],
        [InlineKeyboardButton("8th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/8th/Server2"))]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 2 \n\n**"
        "Check your Rajasthan Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /rj_help command to get help."
    )

    await message.reply_text(text, reply_markup=keyboard)
@app.on_callback_query(filters.regex("^rj_server2$"))
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/Server2"))
        ],
        [
            InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/Server2"))
        ],
        [InlineKeyboardButton("8th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/8th/Server2"))]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 2 \n\n**"
        "Check your Rajasthan Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /rj_help command to get help."
    )

    await message.message.edit_text(text, reply_markup=keyboard)
@app.on_message(filters.command(["rj_Server3", "rj_Server3"]) & filters.private)
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
        "Use /rj_help command to get help."
    )

    await message.reply_text(text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("server3$"))
async def server3_query_handler_query(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/10th/Server3"))
        ],
        [
            InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/RAJ/2025/12th/Server3"))
        ],
        [
          InlineKeyboardButton("🔙Back",callback_data="server3")
        ]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 3 \n\n**"
        "Check your Rajasthan Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /rj_help command to get help."
    )

    await callback_query.message.edit_text(text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^rj_board_result$"))
async def rajasthan_more_handler_query(client, callback_query):
    await callback_query.answer()  # Spinner हटाने के लिए
    rbse= InlineKeyboardMarkup([
            [
                InlineKeyboardButton(f"12th Result {new_year}", web_app=WebAppInfo(
                    url=f"https://geetasaini2042.github.io/Results/RAJ/{new_year}/12th/"
                ))
            ],
            [
                InlineKeyboardButton(f"10th Result {new_year}", web_app=WebAppInfo(
                    url=f"https://geetasaini2042.github.io/Results/RAJ/{new_year}/10th/"
                ))
            ],
            [
                InlineKeyboardButton(f"8th Result {new_year}", web_app=WebAppInfo(
                    url=f"https://geetasaini2042.github.io/Results/RAJ/{new_year}/8th/"
                )),
                InlineKeyboardButton(f"5th Result {new_year}", web_app=WebAppInfo(
                    url=f"https://geetasaini2042.github.io/Results/RAJ/{new_year}/5th/"
                ))
            ],
            [
                InlineKeyboardButton("🔙 Back", callback_data="boards_results")
            ]
        ])
    await callback_query.message.edit_text(
        "Welcome to **Rajasthan Result**\n\n"
        "Check your Rajasthan Board Result for 10th, 12th, 8th and 5th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /rj_NAMEWISE to get your Result by Name."
        "Use /rj_help command to get help.",
        reply_markup=rbse
    )
    
@app.on_callback_query(filters.regex("^rj_board_results$"))
async def rajasthan_more_handler_query(client, callback_query):
    await callback_query.answer()  # Spinner हटाने के लिए
    rbse= InlineKeyboardMarkup([
            [
                InlineKeyboardButton(f"12th Result {new_year}", web_app=WebAppInfo(
                    url=f"https://geetasaini2042.github.io/Results/RAJ/{new_year}/12th/"
                ))
            ],
            [
                InlineKeyboardButton(f"10th Result {new_year}", web_app=WebAppInfo(
                    url=f"https://geetasaini2042.github.io/Results/RAJ/{new_year}/10th/"
                ))
            ],
            [
                InlineKeyboardButton(f"8th Result {new_year}", web_app=WebAppInfo(
                    url=f"https://geetasaini2042.github.io/Results/RAJ/{new_year}/8th/"
                )),
                InlineKeyboardButton(f"5th Result {new_year}", web_app=WebAppInfo(
                    url=f"https://geetasaini2042.github.io/Results/RAJ/{new_year}/5th/"
                ))
            ],
            [
                InlineKeyboardButton("🔙 Back", callback_data="start")
            ]
        ])
    await callback_query.message.edit_text(
        "Welcome to **Rajasthan Result**\n\n"
        "Check your Rajasthan Board Result for 10th, 12th, 8th and 5th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /rj_NAMEWISE to get your Result by Name."
        "Use /rj_help command to get help.",
        reply_markup=rbse
    )
    
@app.on_message(filters.command(["rj_available_commands", "rj_commands"]) & filters.private)
async def rj_commands_handler(client, message):
    await message.reply_text(
        "**📋 Rajasthan Bot Commands (2025 Edition)**\n\n"

        "🔰 **Main & Help**\n"
        "• /rj_start – Bot शुरू करें (main menu)\n"
        "• /rj_help – Rajasthan board help guide\n"
        "• /rj_available_commands – सभी Rajasthan commands की लिस्ट\n\n"

        "🧑‍🎓 **2025 Results**\n"
        "• /rj_result2025 – View 10th, 12th, 8th, 5th Result 2025\n"
        "• /rj_NameWise – नाम से रिजल्ट देखें\n"
        "• /rj_SchoolWise – स्कूल का पूरा रिजल्ट एक साथ देखें\n\n"

        "🌐 **Servers**\n"
        "• /rj_Server2 – Alternate Server 2 for Results\n"
        "• /rj_Server3 – Alternate Server 3 for Results\n\n"

        "📜 **Previous Years Results**\n"
        "• /rj_OldResult – पुराने साल के RollNo से रिजल्ट\n"
        "• /rj_OldResultNamewise – पुराने साल के NameWise रिजल्ट\n\n"

        "📢 **Extra Tools**\n"
        "• /rj_Feedback – Feedback भेजें\n"
        "• /rj_ContactAdmin – Admin से संपर्क करें\n"
        "• /rj_About – Rechecking/Revaluation info\n\n"

        "🧭 **Quick Note**\n"
        "अगर कोई Server काम न करे तो /rj_Server2 या /rj_Server3 try करें।\n"
        "सभी features के लिए Bot को update करते रहें।\n\n"
        "📞 सहायता: @aks979"
    )

@app.on_callback_query(filters.regex("^rj_commands$"))
async def rj_commands_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("️⏪️ Previous", callback_data="commands"),
            InlineKeyboardButton("Next ⏩️", callback_data="up_commands")
        ]
    ])
    await message.message.edit_text(
        "**📋 Rajasthan Bot Commands (2025 Edition)**\n\n"

        "🔰 **Main & Help**\n"
        "• /rj_start – Bot शुरू करें (main menu)\n"
        "• /rj_help – Rajasthan board help guide\n"
        "• /rj_available_commands – सभी Rajasthan commands की लिस्ट\n\n"

        "🧑‍🎓 **2025 Results**\n"
        "• /rj_result2025 – View 10th, 12th, 8th, 5th Result 2025\n"
        "• /rj_NameWise – नाम से रिजल्ट देखें\n"
        "• /rj_SchoolWise – स्कूल का पूरा रिजल्ट एक साथ देखें\n\n"

        "🌐 **Servers**\n"
        "• /rj_Server2 – Alternate Server 2 for Results\n"
        "• /rj_Server3 – Alternate Server 3 for Results\n\n"

        "📜 **Previous Years Results**\n"
        "• /rj_OldResult – पुराने साल के RollNo से रिजल्ट\n"
        "• /rj_OldResultNamewise – पुराने साल के NameWise रिजल्ट\n\n"

        "📢 **Extra Tools**\n"
        "• /rj_Feedback – Feedback भेजें\n"
        "• /rj_ContactAdmin – Admin से संपर्क करें\n"
        "• /rj_About – Rechecking/Revaluation info\n\n"

        "🧭 **Quick Note**\n"
        "अगर कोई Server काम न करे तो /rj_Server2 या /rj_Server3 try करें।\n"
        "सभी features के लिए Bot को update करते रहें।\n\n"
        "📞 सहायता: @aks979",
        reply_markup=keyboard
    )
