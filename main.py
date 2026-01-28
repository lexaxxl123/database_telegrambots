import telebot
import sqlite3

API_TOKEN = 'ENTER_YOUR_TOKEN(DON´T WANT TO SHOW MINE)'

bot = telebot.TeleBot(API_TOKEN)

def init_db():
    connection = sqlite3.connect('bot_database.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tg_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            name TEXT,
            username TEXT
        )
    """)
    connection.commit()
    connection.close()

init_db()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_username = message.from_user.username

    connection = sqlite3.connect('bot_database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tg_users WHERE telegram_id = ?", (user_id,))
    user = cursor.fetchone()

    if not user:
        cursor.execute("INSERT INTO tg_users (telegram_id, name, username) VALUES (?, ?, ?)", (user_id, user_name, user_username))
        connection.commit()
        bot.send_message(message.chat.id, f"Hello, {user_name}! You are now registered.")
    else:
        bot.send_message(message.chat.id, f"Welcome back, {user_name}! You are already in the database.")

    connection.close()

if __name__ == '__main__':
    bot.infinity_polling()
