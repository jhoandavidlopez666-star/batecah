import os
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from flask import Flask

# 1. Configuración del servidor web falso para mantener contento a Render
app = Flask(_name_)

@app.route('/')
def home():
    return "¡Batecah Bot está activo y operando 24/7!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# 2. Funciones de tu bot de Telegram
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Epa, papá! Batecah activo y listo para la acción. 🦾🔥")

# 3. Arranque principal
if _name_ == '_main_':
    # Arrancamos Flask en segundo plano para que Render no cierre el servicio
    web_thread = threading.Thread(target=run_web)
    web_thread.daemon = True
    web_thread.start()

    # Token de tu bot
    TOKEN = "8908447215:AAG6U-iWLLzuH9kOZ1bRpU9L_1haGPGccY"

    application = ApplicationBuilder().token(TOKEN).build()

    # Comando /start
    application.add_handler(CommandHandler('start', start))

    print("Iniciando bot en modo polling...")
    application.run_polling()
