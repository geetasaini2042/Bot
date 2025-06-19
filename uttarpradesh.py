#       uttarpradesh.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from datetime import datetime, time
import pytz
from script import app

@app.on_message( filters.private & (
        filters.command("up_start") |
        (filters.command("start") & filters.regex(r"^/start(@\w+)?\s+up_board_result$"))
    )
)
async def start_handler(client, message):
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    keyboard1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Check Result Now", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2026/10th/"))]
        ]
    )
    keyboard2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("10th Server 1", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2026/10th/"))],
            [InlineKeyboardButton("10th Server 2", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2026/10th/Server2"))]
            
        
        ]
    )
    """
    keyboard1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Check Result Now", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2026/12th/"))]
        ]
    )
    keyboard2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("12th Server 1", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/12th/"))],
            [InlineKeyboardButton("12th Server 2", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2026/12th/Server2"))]
            
        
        ]
    )"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/10th/"))],
            [InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/12th/"))]
        ]
    )
    await message.reply_text(
            "Welcome to **SingodiyaTech Result Bot!**\n\n"
            "Check your UP Board Result for 10th and 12th in one click.\n\n"
            "**Steps:**\n"
            "1. Tap the button below\n"
            "2. Enter your roll number\n"
            "3. Get your marks instantly as PDF or online view.\n\n"
            "Use /up_help command to get help.\n"
            "If current server getting failed, please Use /up_Server2 command.",
            reply_markup=keyboard
        )

    if now.date() == datetime(2025, 5, 30, tzinfo=ist).date():
        if time(1, 0) <= now.time() < time(8, 0):
            await message.reply_text(
                "**आज कक्षा 5 का परिणाम जारी किया जायेगा!**\n\n"
                "परिणाम दोपहर **12:30 बजे तक** आएगा। विद्यार्थी अपने Roll Number से अपना Result निकाल सकते हैं।\n\n"
                "**Class 12th result will be declared today by 12:30 PM.**\n"
                "Please keep your roll number ready.",
                reply_markup=keyboard1
            )

        elif time(8, 0) <= now.time() < time(10, 30):
            await message.reply_text(
                "**कक्षा 5 का परिणाम दोपहर बाद जारी किया जाएगा।**\n"
                "दोपहर **12:30 बजे तक** परिणाम आएगा कृपया प्रतीक्षा करें...\n\n"
                "**Class 12th result will be released post noon.**\n"
                "Expected by 12:30 PM. Please stay tuned.",
                reply_markup=keyboard1
            )

        elif time(10, 30) <= now.time() < time(11, 45):
            await message.reply_text(
                "**कक्षा 5 का परिणाम जल्द ही जारी किया जाएगा!**\n"
                "दोपहर **12:30 बजे** तक परिणाम देखने के लिए तैयार रहें।\n\n"
                "**Class 12th result is coming soon!**\n"
                "Be ready to check it by 12:30 PM.",
                reply_markup=keyboard1
            )

        elif time(11, 45) <= now.time() < time(12,40):
            await message.reply_text(
                "**कक्षा 5 का रिजल्ट कुछ ही देर में जारी किया जाएगा...**\n"
                "कृपया इंतजार करें..\n\n"
                "**Please Wait...**\n\n"
                "**Class 12th result is about to go live.**\n"
                "Please wait patiently and avoid refreshing repeatedly.",
                reply_markup=keyboard2
            )

        elif time(12, 40) <= now.time() <= time(22, 0):
            await message.reply_text(
                "**कक्षा 5 का परिणाम अब जारी कर दिया गया है!**\n"
                "नीचे दिए गए विकल्प से अपना रोल नंबर डालकर तुरंत रिजल्ट देखें।\n\n"                
                "**Class 12th result is now live!**\n"
                "Enter your roll number below to view it instantly.\n\n",
                reply_markup=keyboard2
            )
    elif now.date() == datetime(2025, 5, 29, tzinfo=ist).date():
        await message.reply_text(
                "**कल कक्षा 5 का परिणाम जारी किया जायेगा!**\n\n"
                "परिणाम दोपहर **12:30 बजे तक** आएगा। विद्यार्थी अपने Roll Number से अपना Result निकाल सकते हैं।\n\n"
                "**Class 12th result will be declared tomorrow by 12:30 PM.**\n"
                "Please keep your roll number ready.",
                reply_markup=keyboard1
        )
        
@app.on_message(filters.command(["up_NAMEWISE", "up_NameWise" , "up_Namewise", "up_namewise"]) & filters.private)
async def start_handler(client, message):
    text = """
Welcome to **SingodiyaTech Result Bot!**\n\n            
Check your UP Board Result for 10th & 12th in one click by name.\n\n
**NAMEWISE RESULT 2025**

**Steps:**
1. Tap the button below
2. Enter your Name
3. Confirm your Name and Fathers Name.
4. Click on get.
             
**Use /up_help command to get help.**
"""

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    "10th Result 2025",
                    web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/10th/NameWise/")
                )
            ],
            [
                InlineKeyboardButton(
                    "12th Result 2025",
                    web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/12th/NameWise")
                )
            ]
        ]
    )

    await message.reply_text(
        text,
        reply_markup=keyboard
    )

@app.on_message(filters.command(["up_help", "up_Help"]) & filters.private )
async def help_handler(client, message):
    await message.reply_text(
        "**Help Guide For UP Board**\n\n"
        "• Use 10th or 12th buttons to open result web apps.\n"
        "• Use /up_NameWise to get your result by Name.\n"
        "• Use /up_result2025 to get 2025 results\n"
        "• Use /up_Server2 if the current server is not working\n"
        "• Use /up_OldResult command to get Previous Years Results.\n"
        "• Use /up_oldResultNamewise command to get Previous Years Results By Name.\n"
        "• **Still need help? Contact our support @aks979.**"
    )



@app.on_message(filters.command(["up_result2025", "up_Result2025"]) & filters.private)
async def old_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th RollWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/10th/")),
            InlineKeyboardButton("10th NameWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/10th/NameWise"))
        ],
        [
            InlineKeyboardButton("12th RollWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/12th/")),
            InlineKeyboardButton("12th NameWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/12th/NameWise"))
        ]

    ])
    
    await message.reply_text(
        "Chack Your Result for 2025.\n** Select a Button Below**\n\nEach button will open a web app for that specific Class.",
        reply_markup=keyboard
    )
@app.on_message(filters.command(["up_OldResult", "up_old_result"]) & filters.private)
async def old_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("2024 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2024/10th/")),
            InlineKeyboardButton("2024 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2024/12th/"))
        ],
        [
            InlineKeyboardButton("2023 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2023/10th/")),
            InlineKeyboardButton("2023 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2023/12th/"))
        ],
        [
            InlineKeyboardButton("2022 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2022/10th/")),
            InlineKeyboardButton("2022 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2022/12th/"))
        ]
    ])
    
    await message.reply_text(
        "Previous Year Results\n\n"
        "Select year below to check 10th or 12th result:\n"
        "Each button will open a web app for that specific year.",
        reply_markup=keyboard
    )
@app.on_message(filters.command(["up_OldResultNamewise", "up_old_result_namewise"]) & filters.private)
async def old_result_handler(client, message):
    text = """
"**Previous Year Results (Name Wise)**
Select year below to check 10th or 12th result:
Each button will open a web app for that specific year (Name Wise).
"""
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("2024 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2024/10th/NameWise/")),
            InlineKeyboardButton("2024 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2024/12th/NameWise/"))
        ],
        [
            InlineKeyboardButton("2023 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2023/10th/NameWise/")),
            InlineKeyboardButton("2023 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2023/12th/NameWise/"))
        ],
        [
            InlineKeyboardButton("2022 - 10th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2022/10th/NameWise/")),
            InlineKeyboardButton("2022 - 12th", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2022/12th/NameWise/"))
        ]
    ])
    
    await message.reply_text(text,
        reply_markup=keyboard
    )

@app.on_message(filters.command(["up_Server2", "up_server2"]) & filters.private)
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/10th/Server2"))
        ],
        [
            InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/12th/Server2"))
        ]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 2 \n\n**"
        "Check your UP Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /up_help command to get help."
    )

    await message.reply_text(text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^up_server2$"))
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/10th/Server2"))
        ],
        [
            InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/12th/Server2"))
        ],
         [
          InlineKeyboardButton("🔙Back",callback_data="server2")
        ]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 2 \n\n**"
        "Check your UP Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /up_help command to get help."
    )

    await message.message.reply_text(text, reply_markup=keyboard)
@app.on_callback_query(filters.regex("^up_server2$"))
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/10th/Server2"))
        ],
        [
            InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/12th/Server2"))
        ],
           [
          InlineKeyboardButton("🔙Back",callback_data="server2")
        ]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 2 \n\n**"
        "Check your UP Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /up_help command to get help."
    )

    await message.message.reply_text(text, reply_markup=keyboard)
    
    
    
    
up_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/10th/"))],
            [InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/12th/"))],
            [
                InlineKeyboardButton("🔙 Back", callback_data="boards_results")
            ]
        ]
    )
@app.on_callback_query(filters.regex("^up_board_result$"))
async def rajasthan_more_handler(client, callback_query):
    await callback_query.answer()  # Spinner हटाने के लिए
    await callback_query.message.edit_text(
        "Welcome to **UP Board Result**\n\n"
        "Check your UP Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /up_NAMEWISE to get your Result by Name."
        "Use /up_help command to get help.",
        reply_markup=up_keyboard
    )
up_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("10th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/10th/"))],
            [InlineKeyboardButton("12th Result 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/UP/2025/12th/"))],
            [
                InlineKeyboardButton("🔙 Back", callback_data="start")
            ]
        ]
    )
@app.on_callback_query(filters.regex("^up_board_results$"))
async def rajasthan_more_handler(client, callback_query):
    await callback_query.answer()  # Spinner हटाने के लिए
    await callback_query.message.edit_text(
        "Welcome to **UP Board Result**\n\n"
        "Check your UP Board Result for 10th & 12th in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /up_NAMEWISE to get your Result by Name."
        "Use /up_help command to get help.",
        reply_markup=up_keyboard
    )
@app.on_message(filters.command(["up_available_commands", "up_commands"]) & filters.private)
async def up_commands_handler(client, message):
    await message.reply_text(
        "**📋 up Bot Commands (2025 Edition)**\n\n"

        "🔰 **Main & Help**\n"
        "• /up_start – Start the bot (main menu)\n"
        "• /up_help – Help guide for up Board\n"
        "• /up_available_commands – List of all up commands\n\n"

        "🧑‍🎓 **2025 Results**\n"
        "• /up_result2025 – View 10th, 12th, 8th, 5th Results 2025\n"
        "• /up_NameWise – Check result by name\n"
        "• /up_SchoolWise – View full school result\n\n"

        "🌐 **Servers**\n"
        "• /up_Server2 – Alternate Result Server 2\n"
        "• /up_Server3 – Alternate Result Server 3\n\n"

        "📜 **Previous Years Results**\n"
        "• /up_OldResult – Past year results by Roll Number\n"
        "• /up_OldResultNamewise – Past year results by Name\n\n"

        "📢 **Extra Tools**\n"
        "• /up_Feedback – Send feedback\n"
        "• /up_ContactAdmin – Contact admin\n"
        "• /up_About – Rechecking/Revaluation info\n\n"

        "🧭 **Quick Note**\n"
        "If a server doesn’t work, try /up_Server2 or /up_Server3.\n"
        "Keep updating the bot for all new features.\n\n"
        "📞 Help: @aks979"
    )

@app.on_callback_query(filters.regex("^up_commands$"))
async def up_commands_callback(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("️⏪️ Previous", callback_data="rj_commands"),
            InlineKeyboardButton("Next ⏩️", callback_data="ap_commands")
        ]
    ])
    await message.message.edit_text(
        "**📋 UP Bot Commands (2025 Edition)**\n\n"

        "🔰 **Main & Help**\n"
        "• /up_start – Start the bot (main menu)\n"
        "• /up_help – Help guide for up Board\n"
        "• /up_available_commands – List of all up commands\n\n"

        "🧑‍🎓 **2025 Results**\n"
        "• /up_result2025 – View 10th, 12th, 8th, 5th Results 2025\n"
        "• /up_NameWise – Check result by name\n"

        "🌐 **Servers**\n"
        "• /up_Server2 – Alternate Result Server 2\n"

        "📜 **Previous Years Results**\n"
        "• /up_OldResult – Past year results by Roll Number\n"
        "• /up_OldResultNamewise – Past year results by Name\n\n"

        "📢 **Extra Tools**\n"
        "• /Feedback – Send feedback\n"
        "• /ContactAdmin – Contact admin\n"
        "• /About – Rechecking/Revaluation info\n\n"

        "🧭 **Quick Note**\n"
        "If a server doesn’t work, try /up_Server2 \n"
        "Keep updating the bot for all new features.\n\n"
        "📞 Help: @aks979",
        reply_markup=keyboard
    )
