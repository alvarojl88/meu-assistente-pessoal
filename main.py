import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)
from comandos_tarefas import add_tarefa, listar_tarefas
# from comandos_despesas import add_despesa, listar_despesas
# importe os outros comandos se necessário

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
PORT = int(os.environ.get("PORT", 8080))
HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

app = ApplicationBuilder().token(TOKEN).build()

# registre os handlers
app.add_handler(CommandHandler("add_tarefa", add_tarefa))
app.add_handler(CommandHandler("listar_tarefas", listar_tarefas))
# app.add_handler(CommandHandler("add_despesa", add_despesa))
# app.add_handler(CommandHandler("listar_despesas", listar_despesas))

if __name__ == "__main__":
    # Executa como webhook (recomendado para Render)
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://{HOSTNAME}/{TOKEN}",
    )


