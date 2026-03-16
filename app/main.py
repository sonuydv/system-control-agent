import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, MessageHandler, filters

from agent import run_agent


# Load environment keys from .env to process env
load_dotenv()

async def reply(update:Update,context:ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_name = user.username
    user_id = user.id
    user_message = update.message.text
    print(f"User: ({user_id}:{user_name}) : {user_message}")
    admin_id = os.getenv("TELEGRAM_ADMIN_ID")
    admin_username = os.getenv("TELEGRAM_ADMIN_USERNAME")
    if str(user_id) == admin_id and user_name == admin_username:
        response =  run_agent(user_message)
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("Sorry, you are not authorized to use the agent.")


TELEGRAM_BOT_KEY = os.getenv("TELEGRAM_BOT_TOKEN")
app = ApplicationBuilder().token(TELEGRAM_BOT_KEY).build()

handler = MessageHandler(filters.TEXT & ~filters.COMMAND,reply)
app.add_handler(handler)

print("Bot is running")

app.run_polling()



