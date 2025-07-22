import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configurar logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Comando de início
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou seu assistente pessoal. Digite /ajuda para ver os comandos disponíveis.")

# Comando de ajuda
async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    comandos = [
        "/start - Iniciar o assistente",
        "/ajuda - Ver comandos disponíveis",
        "/planejamento_semanal - Iniciar planejamento semanal",
        "/registrar_sono - Registrar horário de dormir/acordar",
        "/registrar_compra - Registrar compra",
        "/registrar_tarefa - Registrar nova tarefa"
    ]
    await update.message.reply_text("\n".join(comandos))

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Token do bot não definido. Defina a variável BOT_TOKEN.")
    
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ajuda", ajuda))
    
    print("Assistente pessoal iniciado...")
    app.run_polling()

if __name__ == '__main__':
    main()