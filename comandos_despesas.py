from telegram import ContextTypes
from db import conectar

async def add_despesa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        valor = float(context.args[0])
        descricao = " ".join(context.args[1:])
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO despesas (valor, descricao) VALUES (?, ?)", (valor, descricao))
        con.commit()
        con.close()
        await update.message.reply_text("Despesa registrada.")
    except:
        await update.message.reply_text("Use: /add_despesa valor descrição")

async def listar_despesas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, valor, descricao, data FROM despesas ORDER BY data DESC")
    despesas = cur.fetchall()
    con.close()
    if not despesas:
        await update.message.reply_text("Nenhuma despesa encontrada.")
        return
    resposta = "\n".join([f"{id} - R${valor:.2f} - {desc} ({data})" for id, valor, desc, data in despesas])
    await update.message.reply_text(resposta)