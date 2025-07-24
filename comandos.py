
from telegram import Update
from telegram.ext import ContextTypes
from db import conectar

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou seu assistente pessoal.")

async def listar_tarefas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, descricao, data_criacao FROM tarefas")
    tarefas = cur.fetchall()
    con.close()
    if tarefas:
        msg = "\n".join([f"{t[0]} - {t[1]} ({t[2]})" for t in tarefas])
    else:
        msg = "Nenhuma tarefa encontrada."
    await update.message.reply_text(msg)

async def adicionar_tarefa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        descricao = " ".join(context.args)
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
        con.commit()
        con.close()
        await update.message.reply_text("Tarefa adicionada!")
    else:
        await update.message.reply_text("Uso: /add_tarefa descrição da tarefa")

async def listar_despesas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, valor, descricao, data FROM despesas")
    despesas = cur.fetchall()
    con.close()
    if despesas:
        msg = "\n".join([f"{d[0]} - R${d[1]:.2f} - {d[2]} ({d[3]})" for d in despesas])
    else:
        msg = "Nenhuma despesa registrada."
    await update.message.reply_text(msg)

async def adicionar_despesa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        valor = float(context.args[0])
        descricao = " ".join(context.args[1:])
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO despesas (valor, descricao) VALUES (?, ?)", (valor, descricao))
        con.commit()
        con.close()
        await update.message.reply_text("Despesa adicionada!")
    except:
        await update.message.reply_text("Uso: /add_despesa valor descrição")

async def listar_sono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT dormir, acordar FROM sono ORDER BY id DESC LIMIT 5")
    registros = cur.fetchall()
    con.close()
    if registros:
        msg = "\n".join([f"Dormiu: {r[0]} | Acordou: {r[1]}" for r in registros])
    else:
        msg = "Nenhum registro de sono."
    await update.message.reply_text(msg)

async def registrar_dormir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO sono (dormir) VALUES (datetime('now'))")
    con.commit()
    con.close()
    await update.message.reply_text("Horário de dormir registrado.")

async def registrar_acordar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id FROM sono WHERE acordar IS NULL ORDER BY id DESC LIMIT 1")
    row = cur.fetchone()
    if row:
        cur.execute("UPDATE sono SET acordar = datetime('now') WHERE id = ?", (row[0],))
        con.commit()
        await update.message.reply_text("Horário de acordar registrado.")
    else:
        await update.message.reply_text("Nenhum registro de sono encontrado.")
    con.close()

async def listar_compras(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, item, comprado FROM compras")
    compras = cur.fetchall()
    con.close()
    if compras:
        msg = "\n".join([f"{c[0]} - {c[1]} {'✅' if c[2] else '❌'}" for c in compras])
    else:
        msg = "Nenhuma compra encontrada."
    await update.message.reply_text(msg)

async def adicionar_compra(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        item = " ".join(context.args)
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO compras (item) VALUES (?)", (item,))
        con.commit()
        con.close()
        await update.message.reply_text("Item adicionado à lista de compras.")
    else:
        await update.message.reply_text("Uso: /add_compra nome do item")

async def marcar_comprado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        id_item = int(context.args[0])
        con = conectar()
        cur = con.cursor()
        cur.execute("UPDATE compras SET comprado = 1 WHERE id = ?", (id_item,))
        con.commit()
        con.close()
        await update.message.reply_text("Item marcado como comprado.")
    except:
        await update.message.reply_text("Uso: /comprar ID")

async def limpar_compras(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM compras WHERE comprado = 1")
    con.commit()
    con.close()
    await update.message.reply_text("Itens comprados removidos da lista.")
