import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # PDF ya Document bhejne par ID dega
    if update.message.document:
        file_id = update.message.document.file_id
        await update.message.reply_text(f"Ye rahi Document ID:\n\n`{file_id}`", parse_mode='Markdown')
    # Video bhejne par ID dega
    elif update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(f"Ye rahi Video ID:\n\n`{file_id}`", parse_mode='Markdown')

def main():
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()
    # Har document aur video ko handle karega
    app.add_handler(MessageHandler(filters.Document.ALL | filters.VIDEO, get_id))
    app.run_polling()

if __name__ == '__main__':
    main()
