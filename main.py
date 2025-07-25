from db import criar_tabelas
from comandos import adicionar_comandos
import os
from telegram.ext import ApplicationBuilder

def main():
    criar_tabelas()
    token = os.getenv("BOT_TOKEN") or "SEU_TOKEN_AQUI"
    app = ApplicationBuilder().token(token).build()
    adicionar_comandos(app)
    print("Assistente pessoal iniciado...")
    app.run_polling()

if __name__ == '__main__':
    main()