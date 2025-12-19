import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- 1. Apni saari File IDs yahan dalo ---
JAVA_ID = "BQACAgUAAxkBAANGAuUO54TJUPdOVXBLOcxdT3Xv1PcAAkobAAlm1ShWMvWKko0768M2BA"
HR_QUESTION_SET_ID = "BQACAgUAAxkBAAMKaUUo07edKvsSL5H5OFEBWOcxR5oAAisbAAIm1ShWePuiBfIBqLI2BA" # Nayi ID yahan dalo

ADMIN_ID = 2104563445  # <--- Apni asli ID check kar lena

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # --- 2. Button ka naam yahan add karo ---
    keyboard = [
        ['Java Notes 📚', 'HR_Question Set 📝'], # Naya button yahan dala
        ['Physics Notes 🍎', 'Help 💡']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Bhai bot ready hai! Kya chahiye?", reply_markup=reply_markup)

async def handle_everything(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if update.message.text:
        text = update.message.text
        
        # Java Notes ka logic
        if text == 'Java Notes 📚':
            await context.bot.send_document(chat_id=update.effective_chat.id, document=JAVA_ID, caption="Ye lo Java notes! 🔥")
        
        # --- 3. Naye Question Set button ka logic yahan hai ---
        elif text == 'HR_Question Set 📝':
            await context.bot.send_document(chat_id=update.effective_chat.id, document=QUESTION_SET_ID, caption="Ye raha tumhara Question Set! 📑")
            
        elif text == 'Help 💡':
            await update.message.reply_text("Buttons use karo notes ke liye!")

    # ID generator part (Sirf Admin ke liye)
    elif (update.message.document or update.message.video) and user_id == ADMIN_ID:
        file_id = update.message.document.file_id if update.message.document else update.message.video.file_id
        await update.message.reply_text(f"ID mil gayi:\n`{file_id}`", parse_mode='Markdown')

def main():
    token = os.getenv("BOT_TOKEN")
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_everything))
    application.run_polling()

if __name__ == '__main__':
    main()
