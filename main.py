import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from comandos_tarefas import add_tarefa, listar_tarefas
# importe os outros comandos aqui

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
PORT = int(os.environ.get('PORT', '8080'))

app = ApplicationBuilder().token(TOKEN).build()

# registre seus handlers
app.add_handler(CommandHandler("add_tarefa", add_tarefa))
app.add_handler(CommandHandler("listar_tarefas", listar_tarefas))
# adicione os demais comandos aqui

# webhook (obrigatório para Render)
async def start_webhook():
    await app.initialize()
    await app.start()
    await app.updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{TOKEN}",
    )

import asyncio
asyncio.run(start_webhook())

