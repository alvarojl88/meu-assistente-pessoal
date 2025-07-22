@echo off
echo.
echo Iniciando envio do projeto para o GitHub...
echo.

:: Verifica se Git está instalado
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Git não está instalado ou não está no PATH.
    pause
    exit /b
)

:: Inicializa o repositório
git init

:: Define a URL do repositório remoto
git remote add origin https://github.com/alvarojl88/meu-assistente-pessoal.git

:: Adiciona os arquivos ao controle de versão
git add .

:: Cria o commit inicial
git commit -m "Primeiro envio do projeto"

:: Define o nome da branch principal
git branch -M main

:: Envia os arquivos para o repositório remoto
git push -u origin main

echo.
echo Projeto enviado com sucesso!
pause
