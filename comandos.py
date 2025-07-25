from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from comandos_tarefas import *
from comandos_despesas import *
from comandos_compras import *
from comandos_sono import *

def adicionar_comandos(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add_tarefa", add_tarefa))
    app.add_handler(CommandHandler("listar_tarefas", listar_tarefas))
    app.add_handler(CommandHandler("add_despesa", add_despesa))
    app.add_handler(CommandHandler("listar_despesas", listar_despesas))
    app.add_handler(CommandHandler("add_compra", add_compra))
    app.add_handler(CommandHandler("listar_compras", listar_compras))
    app.add_handler(CommandHandler("marcar_comprado", marcar_comprado))
    app.add_handler(CommandHandler("dormir", dormir))
    app.add_handler(CommandHandler("acordar", acordar))
    app.add_handler(CommandHandler("historico_sono", historico_sono))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou seu assistente pessoal.")