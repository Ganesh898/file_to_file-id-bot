import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- Yahan apni details dalo ---
ADMIN_ID = 2104563445  # <--- Apni asli Telegram User ID yahan dalo
JAVA_ID = "BQACAgUAAxkBAANGAuUO54TJUPdOVXBLOcxdT3Xv1PcAAkobAAlm1ShWMvWKko0768M2BA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['Java Notes 📚', 'Physics Notes 🍎'], ['Help 💡']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome! Notes chahiye toh buttons use karo.",
        reply_markup=reply_markup
    )

async def handle_everything(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # 1. Agar koi Text/Button bheje
    if update.message.text:
        text = update.message.text
        if text == 'Java Notes 📚':
            await context.bot.send_document(chat_id=update.effective_chat.id, document=JAVA_ID, caption="Ye lo Java notes! 🔥")
        elif text == 'Help 💡':
            await update.message.reply_text("Buttons pe click karo bhai!")

    # 2. Agar koi Document/Video bheje
    elif update.message.document or update.message.video:
        # Check karo ki kya bhejne wala ADMIN (Aap) hai?
        if user_id == ADMIN_ID:
            file_id = (update.message.document.file_id if update.message.document 
                       else update.message.video.file_id)
            await update.message.reply_text(f"Owner Sahab, ye rahi ID:\n\n`{file_id}`", parse_mode='Markdown')
        else:
            # Agar koi aur hai, toh use ID mat dikhao
            await update.message.reply_text("Sorry bhai, aapko file bhejni allowed nahi hai. Sirf buttons use karo!")

def main():
    token = os.getenv("BOT_TOKEN")
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_everything))
    application.run_polling()

if __name__ == '__main__':
    main()
