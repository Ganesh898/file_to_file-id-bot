import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- 1. Aapki File IDs ---
ACTIVE_HIGHRING_DSA_ID = "BQACAgUAAyEFAATYPjwnAAMraUWivs60GP4C-RqH9ziyntVumcwAAnMeAAIp3zBWSHAtVtF7LsI2BA"
JAVA_ID = "BQACAgUAAxkBAANGAuUO54TJUPdOVXBLOcxdT3Xv1PcAAkobAAlm1ShWMvWKko0768M2BA"
QUESTION_SET_ID = "BQACAgUAAxkBAAMKaUUo07edKvsSL5H5OFEBWOcxR5oAAisbAAIm1ShWePuiBfIBqLI2BA"
DSA_HANDWRITTEN_ID = "BQACAgUAAyEFAATYPjwnAAM5aUWtDNEn9Cy_bk3A9UHsCznH2ZsAAnUeAAIp3zBW-969xay-gBo2BA"

# --- 2. Aapki Admin ID (Isse bot pehchanta hai ki aap owner ho) ---
ADMIN_ID = 2104563445 

# 1. Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['ACTIVE_HIGHRING_DSA'],
        ['DSA_HANDWRITTEN_ NOTES📑'], 
        ['Java Notes 📚', 'HR_Question Set 📝'], 
        ['Physics Notes 🍎', 'Help 💡']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Bhai Apzone Bot ready hai! Kya chahiye?", reply_markup=reply_markup)

# 2. Main Logic
async def handle_everything(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # --- A. BUTTON LOGIC (Sabke liye kaam karega) ---
    if update.message.text:
        text = update.message.text
        
        if text == 'Java Notes 📚':
            await context.bot.send_document(chat_id=update.effective_chat.id, document=JAVA_ID, caption="Ye lo Java notes! 🔥")
        
        elif text == 'HR_Question Set 📝':
            await context.bot.send_document(chat_id=update.effective_chat.id, document=QUESTION_SET_ID, caption="Ye raha tumhara HR Question Set! 📑")
        
        elif text == 'ACTIVE_HIGHRING_DSA':
            await context.bot.send_document(chat_id=update.effective_chat.id, document=ACTIVE_HIGHRING_DSA_ID, caption="Ye raha tumhara Active hiring dsa set! 📑")

        elif text == 'DSA_HANDWRITTEN_ NOTES📑':
            await context.bot.send_document(chat_id=update.effective_chat.id, document=DSA_HANDWRITTEN_ID, caption="Ye lo DSA Handwritten Notes! ✍️🔥")
        
        elif text == 'Help 💡':
            await update.message.reply_text("Bhai, niche diye gaye buttons pe click karo notes mil jayenge!")

    # --- B. ADMIN ONLY LOGIC (Sirf aapko ID dikhegi) ---
    # Agar koi document/video aata hai AUR bhejne wala user ADMIN_ID hai, tabhi ID dikhao
    if (update.message.document or update.message.video):
        if user_id == ADMIN_ID:
            file_id = update.message.document.file_id if update.message.document else update.message.video.file_id
            await update.message.reply_text(f"Owner Sahab, ID mil gayi:\n\n`{file_id}`", parse_mode='Markdown')
        else:
            # Agar koi normal user file bhejta hai, toh bot silent rahega ya ignore karega
            pass

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN nahi mila!")
        return
        
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_everything))
    
    print("Bot chalu ho raha hai...")
    application.run_polling()

if __name__ == '__main__':
    main()
    
