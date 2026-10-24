import time
import os
import random
import json
import urllib.request
from config import DISCORD_TOKEN

def get_network_stats():
    in_speed = round(random.uniform(0.5, 3.5), 1)
    out_speed = round(random.uniform(0.1, 1.5), 1)
    return in_speed, out_speed

def set_discord_status(text):
    if not DISCORD_TOKEN:
        return
    url = "https://discord.com/api/v9/users/@me/settings"
    headers = {
        "Authorization": DISCORD_TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    payload = {"custom_status": {"text": text}}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="PATCH")
    try:
        with urllib.request.urlopen(req) as response:
            pass
    except Exception as e:
        print(f"[Error]: {e}")

def main():
    print("=== Ghost Protocol Status Script Active ===")
    
    statuses = [
        "Ghost Protocol | System Active 💀",
        "Cyberdaemonth | Dev Mode 💻",
        "Termux Automation 🐍"
    ]
    
    idx = 0
    while True:
        try:
            in_s, out_s = get_network_stats()
            net_text = f"IN : {in_s} KB/s OUT : {out_s} KB/s"
            set_discord_status(net_text)
            print(f"อัปเดตสถานะสำเร็จ -> {net_text}")
            time.sleep(3)
            
            status_text = statuses[idx % len(statuses)]
            set_discord_status(status_text)
            print(f"อัปเดตสถานะสำเร็จ -> {status_text}")
            idx += 1
            time.sleep(3)
            
        except KeyboardInterrupt:
            print("\nShutting down Ghost Protocol...")
            break

if __name__ == "__main__":
    main()

