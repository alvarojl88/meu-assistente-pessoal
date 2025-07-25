from telegram import Update
from telegram.ext import ContextTypes
from db import conectar
from datetime import datetime

async def dormir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO sono (dormir) VALUES (?)", (datetime.now(),))
    con.commit()
    con.close()
    await update.message.reply_text("Boa noite! Horário de dormir registrado.")

async def acordar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id FROM sono WHERE acordar IS NULL ORDER BY id DESC LIMIT 1")
    row = cur.fetchone()
    if row:
        cur.execute("UPDATE sono SET acordar = ? WHERE id = ?", (datetime.now(), row[0]))
        con.commit()
        await update.message.reply_text("Bom dia! Horário de acordar registrado.")
    else:
        await update.message.reply_text("Nenhum registro de sono encontrado.")
    con.close()

async def historico_sono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT dormir, acordar FROM sono ORDER BY dormir DESC LIMIT 7")
    rows = cur.fetchall()
    con.close()
    resposta = ""
    for dormir, acordar in rows:
        resposta += f"Dormiu: {dormir} | Acordou: {acordar or '---'}\n"
    await update.message.reply_text(resposta or "Sem registros de sono.")