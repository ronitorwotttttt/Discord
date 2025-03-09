import requests
import random
import pyfiglet

# Terminal colors
Z = '\033[1;31m'  # Red (Bad username)
F = '\033[2;32m'  # Green (Good username)
B = '\033[2;36m'  # Cyan (Banner)
C = '\033[2;35m'  # Purple (Input prompt)

# Banner
logo = pyfiglet.figlet_format('                     Discord')
print(B + logo)

# User inputs
tok = input(C + '    Enter Your Telegram Bot Token -> ')
id = input(C + '    Enter Your Telegram ID -> ')

# Ask for username length
while True:
    try:
        length = int(input(C + "    Enter Username Length (3-32) -> "))
        if 3 <= length <= 32:
            break
        else:
            print(Z + "⚠️ Please enter a length between 3 and 32!")
    except ValueError:
        print(Z + "⚠️ Invalid input! Enter a number.")

while True:
    user = "".join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for _ in range(length))
    email = f"{user}@gmail.com"
    password = "Plugger_1337"

    url = "https://discord.com/api/v9/auth/register"

    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "origin": "https://discord.com",
        "referer": "https://discord.com/register",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6327.2 Safari/537.36"
    }

    data = {
        "email": email,
        "username": user,
        "password": password,
        "invite": None,
        "consent": True,
        "date_of_birth": "2000-01-01",
        "gift_code_sku_id": None,
        "captcha_key": None  # We're NOT solving CAPTCHA, just checking the response
    }

    response = requests.post(url, headers=headers, json=data).text

    if "USERNAME_ALREADY_TAKEN" in response:
        print(Z + f'Bad User -> {user}')
    elif "captcha-required" in response or "rate-limited" in response:
        print(Z + '⚠️ Blocked by CAPTCHA / Rate Limited! Sleeping...')
        break  # Stop script to avoid getting blocked
    else:
        print(F + f'Good User -> {user}')
        message = f"""
⭐ DISCORD USERNAME AVAILABLE ⭐
✦ Username → {user}
By @DrSudo
"""
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=" + str(message))