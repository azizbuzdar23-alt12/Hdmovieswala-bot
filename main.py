import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to HD Movies Wala Bot 🎬\n\nKoi bhi movie ka naam bhejo, main dhoond kar dunga.\n\nExample: Pushpa 2")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie = update.message.text
    await update.message.reply_text(f"🔍 Searching for: {movie}\n\nThori dair wait karo... HD link aa raha hai ⏳")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))
    print("Bot Started...")
    app.run_polling()
