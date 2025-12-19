import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- 1. Aapki File IDs ---
ACTIVE_HIGHRING_DSA_ID = "BQACAgUAAyEFAATYPjwnAAMraUWivs60GP4C-RqH9ziyntVumcwAAnMeAAIp3zBWSHAtVtF7LsI2BA"
JAVA_ID = "BQACAgUAAxkBAANGAuUO54TJUPdOVXBLOcxdT3Xv1PcAAkobAAlm1ShWMvWKko0768M2BA"
QUESTION_SET_ID = "BQACAgUAAxkBAAMKaUUo07edKvsSL5H5OFEBWOcxR5oAAisbAAIm1ShWePuiBfIBqLI2BA"

# --- 2. Aapki Admin ID ---
ADMIN_ID = 2104563445 

# 1. Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Fixed: Added comma between list rows
    keyboard = [
        ['ACTIVE_HIGHRING_DSA'],
        ['Java Notes 📚', 'HR_Question Set 📝'], 
        ['Physics Notes 🍎', 'Help 💡']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Bhai bot ready hai! Kya chahiye?", reply_markup=reply_markup)

# 2. Main Logic
async def handle_everything(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    
    # A. Buttons logic
    if text == 'Java Notes 📚':
        await context.bot.send_document(chat_id=update.effective_chat.id, document=JAVA_ID, caption="Ye lo Java notes! 🔥")
    
    elif text == 'HR_Question Set 📝':
        await context.bot.send_document(chat_id=update.effective_chat.id, document=QUESTION_SET_ID, caption="Ye raha tumhara HR Question Set! 📑")
    
    elif text == 'ACTIVE_HIGHRING_DSA':
        await context.bot.send_document(chat_id=update.effective_chat.id, document=ACTIVE_HIGHRING_DSA_ID, caption="Ye raha tumhara Active hiring dsa set! 📑")
    
    elif text == 'Help 💡':
        await update.message.reply_text("Bhai, niche diye gaye buttons pe click karo notes mil jayenge!")

    # B. ID Generator (Sirf Admin ke liye - Document ya Video bhejne par)
    if (update.message.document or update.message.video) and user_id == ADMIN_ID:
        file_id = update.message.document.file_id if update.message.document else update.message.video.file_id
        await update.message.reply_text(f"Owner Sahab, ID mil gayi:\n\n`{file_id}`", parse_mode='Markdown')

def main():
    # Token check
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN environment variable mein nahi mila!")
        return
        
    application = Application.builder().token(token).build()
    
    # Handlers
    application.add_handler(CommandHandler("start", start))
    # filters.ALL use kiya hai taaki text aur document dono capture ho sakein
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_everything))
    
    print("Bot chalu ho raha hai...")
    application.run_polling()

if __name__ == '__main__':
    main()
    
