from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, MessageHandler, filters

from agent import run_agent
from env_helper import config

async def reply(update:Update,context:ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_name = user.username
    user_id = user.id
    user_message = update.message.text
    print(f"User: ({user_id}:{user_name}) : {user_message}")
    if str(user_id) == config.TELEGRAM_ADMIN_ID and user_name == config.TELEGRAM_ADMIN_USERNAME:
        response =  run_agent(user_message)
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("Sorry, you are not authorized to use the agent.")


app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

handler = MessageHandler(filters.TEXT & ~filters.COMMAND,reply)
app.add_handler(handler)

print("Bot is running")

app.run_polling()



