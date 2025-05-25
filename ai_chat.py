import requests
import os
from script import user_histories, url
from datetime import datetime
import pytz

def india_time():
    india_timezone = pytz.timezone('Asia/Kolkata')
    india_now = datetime.now(india_timezone)
    return india_now.strftime("[%d/%m/%Y %H:%M:%S]")

def sendAi_message(user_id, user_name, user_msg):
    headers = {"Content-Type": "application/json"}

    # Initialize conversation history if user is new
    if user_id not in user_histories:
        user_histories[user_id] = []

    # Add the user's message to history
    user_histories[user_id].append({
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": user_msg
            }
        ]
    })

    # Current time to inform the AI
    current_time = india_time()

    # System message with timestamp
    system_message = f"""
You are a helpful and empathetic AI assistant that responds to students' questions about their exam results.
You speak in simple, polite Hindi. Only answer what the student asks — do not add extra info.

Current Indian Time: {current_time}

Rules:
1. Only answer the specific question asked (e.g., 12th result = reply only about 12th).
2. Keep replies under 50 characters if possible.
3. Give longer replies only when needed (e.g., explaining confusion).
4. Information you must know:
   - 12th result: Declared on 22 May at 5 PM
   - 10th result: Expected between 25–30 May
   - Use /Server2 or /Server3 if main server fails
   - Previous year results:
     - Roll no: /OldResult
     - Name wise: /OldResultNamewise
     - School wise: Not available for previous years
   - Latest year school-wise: /SchoolWise
   - 8th result: Declared on 26 May at 5 PM
   - 5th result: Date not yet known
   - 10th & 12th results can be checked directly on this bot
   - 8th & 5th results will be linked here once declared

Keep responses short, polite, and focused.
"""

    # Prepare API request payload
    payload = {
        "model": "gpt-4",
        "system": system_message.strip(),
        "messages": user_histories[user_id]
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        assistant_msg = result.get("choices", [{}])[0].get("message", {}).get("content", "")

        # Add assistant's reply to history
        user_histories[user_id].append({
            "role": "assistant",
            "content": assistant_msg
        })

        return assistant_msg

    except requests.RequestException as e:
        print(f"{india_time()} API Error: {e}")
        return ""
