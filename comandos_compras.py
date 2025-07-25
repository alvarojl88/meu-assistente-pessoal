from telegram.ext import ContextTypes
from db import conectar

async def add_compra(update: Update, context: ContextTypes.DEFAULT_TYPE):
    item = " ".join(context.args)
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO compras (item) VALUES (?)", (item,))
    con.commit()
    con.close()
    await update.message.reply_text("Item adicionado à lista de compras.")

async def listar_compras(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, item, comprado FROM compras")
    compras = cur.fetchall()
    con.close()
    resposta = "\n".join([f"{id} - {item} [{'OK' if comprado else 'pendente'}]" for id, item, comprado in compras])
    await update.message.reply_text(resposta)

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
        await update.message.reply_text("Use: /marcar_comprado id")