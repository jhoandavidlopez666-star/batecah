import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# Configurar el registro de eventos (logs)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Token oficial de BatecahBot integrado
TOKEN = "8908447215:AAG6U-iWLLzuH9kOZ1bRpU9L_1haGPGccY"

# Diccionario temporal en memoria para guardar los puntos de los usuarios
usuarios_puntos = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    
    # Si es nuevo, inicializamos sus puntos
    if user_id not in usuarios_puntos:
        usuarios_puntos[user_id] = 0

    puntos = usuarios_puntos[user_id]
    
    # Creamos un botón interactivo para simular el "Tap" o la Mini App
    keyboard = [
        [InlineKeyboardButton("⚡ ¡Hacer Tap (+1 BatecahCoin)!", callback_data='tap')],
        [InlineKeyboardButton("💰 Ver Balance / Retirar", callback_data='balance')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    mensaje = (
        f"🔥 ¡Bienvenido a *Batecah, *{user.first_name}! 🔥\n\n"
        f"El minijuego oficial de Tap to Earn está activo.\n"
        f"Tus puntos actuales: *{puntos} BatecahCoins*\n\n"
        f"¡Toca el botón de abajo para empezar a minar y ganar recompensas reales!"
    )
    
    await update.message.reply_text(mensaje, reply_markup=reply_markup, parse_mode='Markdown')

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    if user_id not in usuarios_puntos:
        usuarios_puntos[user_id] = 0

    if query.data == 'tap':
        usuarios_puntos[user_id] += 1
        puntos_actuales = usuarios_puntos[user_id]
        
        keyboard = [
            [InlineKeyboardButton("⚡ ¡Hacer Tap (+1 BatecahCoin)!", callback_data='tap')],
            [InlineKeyboardButton("💰 Ver Balance / Retirar", callback_data='balance')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text=f"🔥 ¡Buen Tap!\nTus puntos actuales: *{puntos_actuales} BatecahCoins*",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    elif query.data == 'balance':
        puntos_actuales = usuarios_puntos[user_id]
        # Regla de negocio: Retiro mínimo $5 y comisión de $1
        await query.message.reply_text(
            f"📊 *Tu Panel Batecah*\n\n"
            f"• Puntos totales: {puntos_actuales}\n"
            f"• Retiro Mínimo: $5 USDT\n"
            f"• Comisión por retiro: $1 USDT\n\n"
            f"Completa tus tareas de anunciantes para habilitar el retiro a tu wallet.",
            parse_mode='Markdown'
        )

def main():
    # Inicializar la aplicación del bot con el Token
    application = ApplicationBuilder().token(TOKEN).build()

    # Manejadores de comandos y botones
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))

    print("🤖 ¡Bot de Batecah iniciado y escuchando eventos...")
    # Arrancar el bot de forma continua (Polling)
    application.run_polling()

if _name_ == '_main_':
    main()
