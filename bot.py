import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(_name_)

TOKEN = "8908447215:AAG6U-iWLLzuH9kOZ1bRpU9L_1haGPGccY"

# Inicializamos la app del bot de forma síncrona para webhooks
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Epa, papá! Batecah activo y operando 24/7 con webhook. 🦾🔥")

application.add_handler(CommandHandler('start', start))

@app.route('/')
def home():
    return "¡Batecah Bot Web Service is running!"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    # Recibe la actualización de Telegram y la procesa
    json_data = request.get_json(force=True)
    update = Update.de_json(json_data, application.bot)
    
    # Ejecutamos el procesamiento del update de forma síncrona
    import asyncio
    asyncio.run(application.initialize())
    asyncio.run(application.process_update(update))
    return 'OK', 200

if _name_ == '_main_':
    # Configuramos el webhook automáticamente en Telegram al arrancar
    PORT = int(os.environ.get('PORT', 10000))
    # Nota: Render te da una URL pública como https://batecah.onrender.com
    # Puedes configurar la URL del webhook si gustas, o dejar que Flask escuche el puerto
    app.run(host='0.0.0.0', port=PORT)
