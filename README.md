# Telegram Bot User Registration System

A Python-based Telegram bot that integrates with an SQLite database to handle user registration automatically. The bot captures user details (ID, Name, Username) upon the first interaction and prevents duplicate entries.

## 📌 Features

* **Automatic Registration:** Captures user data immediately when they send `/start`.
* **Database Integration:** Uses SQLite (`bot_database.db`) to store user information securely.
* **Duplicate Prevention:** Checks if a user already exists before trying to register them (prevents SQL errors).
* **Connection Safety:** Opens and closes database connections per request to avoid threading issues.
* **Infinity Polling:** The bot automatically restarts if the connection drops.

## 🛠️ Technologies Used

* **Python 3.x**
* **pyTelegramBotAPI (telebot)** - For Telegram API interaction.
* **SQLite3** - For local database management.

## 🚀 How to Run

### 1. Prerequisites
Make sure you have Python installed. Then, install the required library: pip install pyTelegramBotAPI


###2. Configuration
Open the main.py file and replace the placeholder with your actual bot token:

API_TOKEN = 'YOUR_REAL_TOKEN_HERE'

3. Launch the Bot
Run the script in your terminal: python main.py

#📝 Usage Example

#1)User starts the bot in Telegram.

#2)User sends /start.

#3)Scenario A (New User):

    Bot saves ID and Name to DB.

    Bot replies: "Hello, [Name]! You are now registered."

#4)Scenario B (Existing User):

    Bot checks DB and finds the ID.

    Bot replies: "Welcome back, [Name]! You are already in the database."

#🛡️ License
This project is open-source and free to use.
