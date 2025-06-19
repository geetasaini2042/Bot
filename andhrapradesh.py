#          andhrapradesh.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from datetime import datetime, time
import pytz
from script import app

@app.on_message( filters.private & (
        filters.command("ap_start") |
        (filters.command("start") & filters.regex(r"^/start(@\w+)?\s+ap_board_result$"))
    )
)
async def start_handler(client, message):
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    
    
    ap_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("SSC EXAM RESULT 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/10th/"))],
            [InlineKeyboardButton("Int 1st Year 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/11th/"))],
            [InlineKeyboardButton("Int 2nd Year 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/12th/"))]

        ]
    )
    await message.reply_text(
            "Welcome to **SingodiyaTech Result Bot!**\n\n"
            "Check your Andhra Pradesh Board Result for SSC Exam(10th class), Inter 1st year(11th class) and Inter 2nd year(12th class) in one click.\n\n"
            "**Steps:**\n"
            "1. Tap the button below\n"
            "2. Enter your roll number\n"
            "3. Get your marks instantly as PDF or online view.\n\n"
            "Use /ap_help command to get help.\n"
            "If current server getting failed, please Use /ap_Server2 command.",
            reply_markup=ap_keyboard
        )
        
@app.on_message(filters.command(["ap_NAMEWISE", "ap_NameWise" , "ap_Namewise", "ap_namewise"]) & filters.private)
async def start_handler(client, message):
    text = """
Welcome to **SingodiyaTech Result Bot!**\n\n            
Check your Andhra Pradesh Board Result for SSC Exam, 1st year & 2nd year in one click by name.\n\n
**NAMEWISE RESULT 2025**

**Steps:**
1. Tap the button below
2. Enter your Name
3. Confirm your Name and Roll Number.
4. Click on get.
             
**Use /ap_help command to get help.**
"""

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    "SSC EXAM RESULT 2025",
                    web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/10th/NameWise/")
                )
            ],   
            [
                InlineKeyboardButton(
                    "Int 1st Year 2025",
                    web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/11th/NameWise")
                )
            ],
            [
                InlineKeyboardButton(
                    "Int 2nd Year 2025",
                    web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/12th/NameWise")
                )
            ]
        ]
    )

    await message.reply_text(
        text,
        reply_markup=keyboard
    )

@app.on_message(filters.command(["ap_help", "ap_help"]) & filters.private )
async def help_handler(client, message):
    await message.reply_text(
        "**Help Guide For Andhra Pradesh Board**\n\n"
        "• Use 10th or 2nd year buttons to open result web apps.\n"
        "• Use /ap_NameWise to get your result by Name.\n"
        "• Use /ap_result2025 to get 2025 results\n"
        "• Use /ap_Server2 if the current server is not working\n"
        "• Use /ap_OldResult command to get Previous Years Results.\n"
        "• **Still need help? Contact our support @aks979.**"
    )


@app.on_message(filters.command(["ap_result2025", "ap_Result2025"]) & filters.private)
async def old_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("SSC Exam RollWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/10th/")),
            InlineKeyboardButton("SSC Exam NameWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/10th/NameWise"))
        ],
        [
            InlineKeyboardButton("1st year RollWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/11th/")),
            InlineKeyboardButton("2nd year NameWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/11th/NameWise"))
        ],
        [
            InlineKeyboardButton("2nd year RollWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/12th/")),
            InlineKeyboardButton("2nd year NameWise", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/12th/NameWise"))
        ]

    ])
    
    await message.reply_text(
        "Chack Your Result for 2025.\n** Select a Button Below**\n\nEach button will open a web app for that specific Class.",
        reply_markup=keyboard
    )
@app.on_message(filters.command(["ap_OldResult", "ap_old_result"]) & filters.private)
async def old_result_handler(client, message):
    keyboard = InlineKeyboardMarkup([
         [
            InlineKeyboardButton("2025 - SSC Exam", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/10th/")),
            InlineKeyboardButton("2025 - 1st year", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/11th/")),
            InlineKeyboardButton("2025 - 2nd year", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/12th/"))
        ],
        [
            InlineKeyboardButton("2024 - SSC Exam", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2024/10th/")),
            InlineKeyboardButton("2024 - 1st year", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2024/11th/")),
            InlineKeyboardButton("2024 - 2nd year", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2024/12th/"))
        ],
        [
            InlineKeyboardButton("2023 - SSC Exam", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2023/10th/")),
            InlineKeyboardButton("2023 - 1st year", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2023/11th/")),
            InlineKeyboardButton("2023 - 2nd year", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2023/12th/"))
        ],
        [
            InlineKeyboardButton("2022 - SSC EXAM", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2022/10th/")),
            InlineKeyboardButton("2022 - 1st year", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2022/11th/")),
            InlineKeyboardButton("2022 - 2nd year", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2022/11th/"))
        ]
    ])
    
    await message.reply_text(
        "Previous Year Results\n\n"
        "Select year below to check SSC Exam, Int 1st Year or Int 2nd Year:\n"
        "Each button will open a web app for that specific year.",
        reply_markup=keyboard
    )


@app.on_message(filters.command(["ap_Server2", "ap_server2"]) & filters.private)
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("SSC EXAM RESULT 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/10th/Server2"))
        ],
        [
            InlineKeyboardButton("Int 1st Year 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/11th/Server2"))
        ],
        [
            InlineKeyboardButton("Int 2nd Year 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/12th/Server2"))
        ]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 2 \n\n**"
        "Check your Andhra Pradesh Board Result for 10th, 1st year & 2nd year in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /ap_help command to get help."
    )

    await message.reply_text(text, reply_markup=keyboard)
@app.on_callback_query(filters.regex("^ap_server2$"))
async def server2_handler(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("SSC EXAM RESULT 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/10th/Server2"))
        ],
        [
            InlineKeyboardButton("Int 1st Year 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/11th/Server2"))
        ],
        [
            InlineKeyboardButton("Int 2nd Year 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/12th/Server2"))
        ],
        [
          InlineKeyboardButton("🔙Back",callback_data="server2")
        ]
    ])

    text = (
        "Welcome to **SingodiyaTech Result Bot!**\n\n **Server 2 \n\n**"
        "Check your Andhra Pradesh Board Result for 10th, 1st year & 2nd year in one click.\n\n"
        "Steps:\n"
        "1. Tap the button below\n"
        "2. Enter your roll number\n"
        "3. Get your marks instantly as PDF or online view.\n"
        "Use /ap_help command to get help."
    )

    await message.message.reply_text(text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^ap_board_result$"))
async def rajasthan_more_handler(client, callback_query):
    await callback_query.answer()  # Spinner हटाने के लिए
    ap_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("SSC EXAM RESULT 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/10th/"))],
            [InlineKeyboardButton("Int 1st Year 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/11th/"))],
            [InlineKeyboardButton("Int 2nd Year 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/12th/"))],
            [InlineKeyboardButton("🔙 Back", callback_data="boards_results")]

        ])
    await callback_query.message.edit_text(
            "Welcome to **SingodiyaTech Result Bot!**\n\n"
            "Check your Andhra Pradesh Board Result for SSC Exam(10th class), Inter 1st year(11th class) and Inter 2nd year(12th class) in one click.\n\n"
            "**Steps:**\n"
            "1. Tap the button below\n"
            "2. Enter your roll number\n"
            "3. Get your marks instantly as PDF or online view.\n\n"
            "Use /ap_NAMEWISE to get your Result by Name."
            "Use /ap_help command to get help.",
        reply_markup=ap_keyboard
    )

@app.on_callback_query(filters.regex("^ap_board_results$"))
async def rajasthan_more_handler(client, callback_query):
    await callback_query.answer()  # Spinner हटाने के लिए
    ap_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("SSC EXAM RESULT 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/10th/"))],
            [InlineKeyboardButton("Int 1st Year 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/11th/"))],
            [InlineKeyboardButton("Int 2nd Year 2025", web_app=WebAppInfo(url="https://geetasaini2042.github.io/Results/AP/2025/12th/"))],
            [InlineKeyboardButton("🔙 Back", callback_data="start")]

        ])
    await callback_query.message.edit_text(
            "Welcome to **SingodiyaTech Result Bot!**\n\n"
            "Check your Andhra Pradesh Board Result for SSC Exam(10th class), Inter 1st year(11th class) and Inter 2nd year(12th class) in one click.\n\n"
            "**Steps:**\n"
            "1. Tap the button below\n"
            "2. Enter your roll number\n"
            "3. Get your marks instantly as PDF or online view.\n\n"
            "Use /ap_NAMEWISE to get your Result by Name."
            "Use /ap_help command to get help.",
        reply_markup=ap_keyboard
    )
@app.on_message(filters.command(["ap_available_commands", "ap_commands"]) & filters.private)
async def ap_commands_handler(client, message):
    await message.reply_text(
        "**📋 ap Bot Commands (2025 Edition)**\n\n"

        "🔰 **Main & Help**\n"
        "• /ap_start – Start the bot (main menu)\n"
        "• /ap_help – Help guide for ap Board\n"
        "• /ap_available_commands – List of all ap commands\n\n"

        "🧑‍🎓 **2025 Results**\n"
        "• /ap_result2025 – View 10th, 12th, 8th, 5th Results 2025\n"
        "• /ap_NameWise – Check result by name\n"
        "• /ap_SchoolWise – View full school result\n\n"

        "🌐 **Servers**\n"
        "• /ap_Server2 – Alternate Result Server 2\n"
        "• /ap_Server3 – Alternate Result Server 3\n\n"

        "📜 **Previous Years Results**\n"
        "• /ap_OldResult – Past year results by Roll Number\n"
        "• /ap_OldResultNamewise – Past year results by Name\n\n"

        "📢 **Extra Tools**\n"
        "• /ap_Feedback – Send feedback\n"
        "• /ap_ContactAdmin – Contact admin\n"
        "• /ap_About – Rechecking/Revaluation info\n\n"

        "🧭 **Quick Note**\n"
        "If a server doesn’t work, try /ap_Server2 or /ap_Server3.\n"
        "Keep updating the bot for all new features.\n\n"
        "📞 Help: @aks979"
    )

@app.on_callback_query(filters.regex("^ap_commands$"))
async def ap_commands_callback(client, message):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("️⏪️Previous️", callback_data="up_commands")
        ]
    ])
    await message.message.edit_text(
        "**📋 Andhra pradesh Bot Commands (2025 Edition)**\n\n"

        "🔰 **Main & Help**\n"
        "• /ap_start – Start the bot (main menu)\n"
        "• /ap_help – Help guide for ap Board\n"
        "• /ap_available_commands – List of all ap commands\n\n"

        "🧑‍🎓 **2025 Results**\n"
        "• /ap_result2025 – View 10th, 12th, 8th, 5th Results 2025\n"
        "• /ap_NameWise – Check result by name\n"

        "🌐 **Servers**\n"
        "• /ap_Server2 – Alternate Result Server 2\n"

        "📜 **Previous Years Results**\n"
        "• /ap_OldResult – Past year results by Roll Number\n"
        "• /ap_OldResultNamewise – Past year results by Name\n\n"

        "📢 **Extra Tools**\n"
        "• /Feedback – Send feedback\n"
        "• /ContactAdmin – Contact admin\n"
        "• /About – Rechecking/Revaluation info\n\n"

        "🧭 **Quick Note**\n"
        "If a server doesn’t work, try /ap_Server2\n"
        "Keep updating the bot for all new features.\n\n"
        "📞 Help: @aks979",
        reply_markup=keyboard
    )
