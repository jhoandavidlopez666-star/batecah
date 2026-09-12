import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Configurar logs para ver qué pasa en Render
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Token de tu bot Batecah
BOT_TOKEN = "8908447215:AAG6U-iWLLzuH9kOZ1bRpU9L_1haGPGccY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"¡Bienvenido a *Batecah*, {user_name}! 🚀\n\n"
        "El minijuego Tap to Earn está listo. Prepárate para farmear puntos."
    )

def main():
    # Construir la aplicación del bot
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Registrar el comando /start
    application.add_handler(CommandHandler("start", start))

    print("¡Batecah Bot está corriendo en la nube de Render!")
    
    # Iniciar el bot en modo polling continuo
    application.run_polling()

if _name_ == '_main_':
    main()
