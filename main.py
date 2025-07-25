import logging
import os

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from comandos import start
from comandos_compras import *
from comandos_despesas import *
from comandos_sono import *
from comandos_tarefas import *

from db import criar_tabelas

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Olá {update.effective_user.first_name}!')

def main():
    criar_tabelas()

    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("Variável de ambiente TELEGRAM_TOKEN não definida")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))

    app.add_handler(CommandHandler("compras_adicionar", compras_adicionar))
    app.add_handler(CommandHandler("compras_listar", compras_listar))
    app.add_handler(CommandHandler("compras_marcar", compras_marcar))
    app.add_handler(CommandHandler("compras_remover", compras_remover))
    app.add_handler(CommandHandler("compras_limpar", compras_limpar))

    app.add_handler(CommandHandler("despesa_adicionar", despesa_adicionar))
    app.add_handler(CommandHandler("despesa_listar", despesa_listar))

    app.add_handler(CommandHandler("sono_registrar", sono_registrar))
    app.add_handler(CommandHandler("sono_listar", sono_listar))

    app.add_handler(CommandHandler("tarefa_adicionar", tarefa_adicionar))
    app.add_handler(CommandHandler("tarefa_listar", tarefa_listar))

    print("Assistente pessoal iniciado...")
    app.run_polling()

if __name__ == '__main__':
    main()
