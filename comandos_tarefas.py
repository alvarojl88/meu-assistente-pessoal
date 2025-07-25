from telegram import Update
from telegram.ext import ContextTypes
from db import conectar

async def add_tarefa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = " ".join(context.args)
    if not texto:
        await update.message.reply_text("Use: /add_tarefa descrição da tarefa")
        return
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO tarefas (descricao) VALUES (?)", (texto,))
    con.commit()
    con.close()
    await update.message.reply_text("Tarefa adicionada!")

async def listar_tarefas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, descricao, data_criacao FROM tarefas ORDER BY data_criacao DESC")
    tarefas = cur.fetchall()
    con.close()
    if not tarefas:
        await update.message.reply_text("Nenhuma tarefa encontrada.")
        return
    resposta = "\n".join([f"{id} - {desc} ({data})" for id, desc, data in tarefas])
    await update.message.reply_text(resposta)