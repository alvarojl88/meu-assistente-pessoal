
from db import criar_tabelas
from comandos import *

criar_tabelas()

import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

token = os.getenv("BOT_TOKEN", "INSIRA_SEU_TOKEN_AQUI")

logging.basicConfig(level=logging.INFO)

def main():
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tarefas", listar_tarefas))
    app.add_handler(CommandHandler("add_tarefa", adicionar_tarefa))
    app.add_handler(CommandHandler("despesas", listar_despesas))
    app.add_handler(CommandHandler("add_despesa", adicionar_despesa))
    app.add_handler(CommandHandler("sono", listar_sono))
    app.add_handler(CommandHandler("dormir", registrar_dormir))
    app.add_handler(CommandHandler("acordar", registrar_acordar))
    app.add_handler(CommandHandler("compras", listar_compras))
    app.add_handler(CommandHandler("add_compra", adicionar_compra))
    app.add_handler(CommandHandler("comprar", marcar_comprado))
    app.add_handler(CommandHandler("limpar_compras", limpar_compras))

    print("Assistente pessoal iniciado...")
    app.run_polling()

if __name__ == '__main__':
    main()
