import os
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bhai bot chalu hai! Ab koi PDF ya Video bhejo, main ID de dunga.")

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        file_id = update.message.document.file_id
        await update.message.reply_text(f"Document ID:\n\n`{file_id}`", parse_mode='Markdown')
    elif update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(f"Video ID:\n\n`{file_id}`", parse_mode='Markdown')

def main():
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL | filters.VIDEO, get_id))
    
    app.run_polling()

if __name__ == '__main__':
    main()
