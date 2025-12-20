import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- 1. Aapki File IDs ---
ACTIVE_HIGHRING_DSA_ID = "BQACAgUAAyEFAATYPjwnAAMraUWivs60GP4C-RqH9ziyntVumcwAAnMeAAIp3zBWSHAtVtF7LsI2BA"
JAVA_ID = "BQACAgUAAxkBAANGAuUO54TJUPdOVXBLOcxdT3Xv1PcAAkobAAlm1ShWMvWKko0768M2BA"
QUESTION_SET_ID = "BQACAgUAAxkBAAMKaUUo07edKvsSL5H5OFEBWOcxR5oAAisbAAIm1ShWePuiBfIBqLI2BA"
C_PROGRAMMING_ID = "BQACAgUAAxkBAAMWaUXKcdw67BK_usCd1loAAU177iA-AAL4HwACr44wVnYgzuLtuuJyNgQ"

# Naye Notes ki IDs
CORE_JAVA_ID = "BQACAgUAAxkBAAMcaUYzb-CoxiyT5dUXSBUvXbwtHl8AAnwdAAKvjjhW-YeUZ_0BH9U2BA"
PYTHON_NOTES_ID = "BQACAgUAAxkBAAMeaUYz4mO627Jx3mdKFEtE1vhVnfgAAn0dAAKvjjhW53Vvld_pHVA2BA"
OOPS_CONCEPT_ID = "BQACAgUAAxkBAAMaaUYy6K1Hxw_QthaEtpS0WWTwERMAAnodAAKvjjhWIkqNlBQlSP82BA"

# --- 2. Aapki Admin ID ---
ADMIN_ID = 2104563445 

# 1. Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Buttons layout ko organize kiya hai taaki screen pe sahi dikhe
    keyboard = [
        ['ACTIVE_HIGHRING_DSA'],
        ['Core_Java_Handwritten_notes'],
        ['Python_H.D_Notes', 'Oops_Concept'],
        ['C_programming_book_Notes'],
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

    elif text == 'C_programming_book_Notes':
        await context.bot.send_document(chat_id=update.effective_chat.id, document=C_PROGRAMMING_ID, caption="Ye lo C Programming Book Notes! 💻📘")

    # Naya Logic for Core Java, Python, and OOPS
    elif text == 'Core_Java_Handwritten_notes':
        await context.bot.send_document(chat_id=update.effective_chat.id, document=CORE_JAVA_ID, caption="Ye lo Core Java Handwritten Notes! ☕✍️")

    elif text == 'Python_H.D_Notes':
        await context.bot.send_document(chat_id=update.effective_chat.id, document=PYTHON_NOTES_ID, caption="Ye lo Python Handwritten Notes! 🐍📖")

    elif text == 'Oops_Concept':
        await context.bot.send_document(chat_id=update.effective_chat.id, document=OOPS_CONCEPT_ID, caption="Ye lo OOPS Concepts ke notes! 🌀📚")
    
    elif text == 'Help 💡':
        await update.message.reply_text("Bhai, niche diye gaye buttons pe click karo notes mil jayenge!")

    # B. ID Generator (Sirf Admin ke liye)
    if (update.message.document or update.message.video) and user_id == ADMIN_ID:
        file_id = update.message.document.file_id if update.message.document else update.message.video.file_id
        await update.message.reply_text(f"Owner Sahab, ID mil gayi:\n\n`{file_id}`", parse_mode='Markdown')

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN environment variable mein nahi mila!")
        return
        
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_everything))
    
    print("Bot chalu ho raha hai...")
    application.run_polling()

if __name__ == '__main__':
    main()
    
