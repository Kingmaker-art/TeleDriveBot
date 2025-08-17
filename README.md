🚀 TeleDriveBot

A self-hosted Telegram Bot that transfers files from Telegram → Google Drive.
Built with Python + Telethon + Google Drive API.

✨ Features

📂 Transfer files/folders directly from Telegram to Google Drive

🔑 Secure OAuth login flow (Google Drive authentication)

📤 Upload any file type (up to your Google Drive quota)

🔄 Resume/retry uploads if interrupted

🖼 Auto thumbnail generation for media (optional)

⚡ No need for Colab, VPS, or third-party services – just run locally

📦 Requirements

Python 3.9+

Google Cloud Project with OAuth credentials (Desktop type)

A Telegram account (for API ID & Hash)

A Telegram Bot Token

⚙️ Setup

Clone this repository

git clone https://github.com/YOUR_USERNAME/TeleDriveBot.git
cd TeleDriveBot


Install dependencies

pip install -r requirements.txt


Add your config:

credentials.json → Google API credentials (from Google Cloud Console)

.env → contains Telegram API keys and Bot Token

Run the bot

python main.py

🤖 Bot Commands

/login → Authenticate with Google Drive

/upload → Upload file/folder to Drive

/status → Check upload progress

/help → Show available commands

🔐 Notes

This bot is for personal use.

Google may block your project if you misuse Drive API.

Respect copyright – only transfer files you own the rights to.

💡 Example Use Cases

Backup Telegram media directly to Google Drive

Store large files securely in the cloud

Automate file organization from Telegram channels

⚖️ License

GPL-3.0 License

✨ If this project helps you, leave a ⭐ on GitHub!
