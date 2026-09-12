import os
import http.server
import socketserver
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# 1. Servidor HTTP nativo para que Render abra el puerto 10000 feliz
PORT = int(os.environ.get("PORT", 10000))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Batecah Bot is alive!")

def run_server():
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Servidor web corriendo en puerto {PORT}")
        httpd.serve_forever()

# 2. Función del bot de Telegram
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Epa, papá! Batecah activo y operando 24/7. 🦾🔥")

# 3. Arranque principal
def main():
    # Lanzamos el servidor web en un hilo secundario
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Arrancamos el bot de Telegram en el hilo principal
    TOKEN = "8908447215:AAG6U-iWLLzuH9kOZ1bRpU9L_1haGPGccY"
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Iniciando bot de Telegram...")
    application.run_polling()

if _name_ == '_main_':
    main()
