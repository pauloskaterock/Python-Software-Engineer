#!/usr/bin/env python3
# rpa_boas_vindas.py - Seu primeiro script profissional

import cowsay
import sys
from datetime import datetime

def main():
    """Função principal do programa"""

    # Cabeçalho
    print("=" * 60)
    print("🤖 PROJETO RPA - PYTHON AUTOMAÇÃO".center(60))
    print("=" * 60)

    # Informações do sistema
    print(f"\n📅 Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"🐍 Versão Python: {sys.version[:5]}")
    print(f"📁 Ambiente: {sys.prefix}")

    # Mascote do Linux
    cowsay.tux("\nPreparado para automatizar tarefas RPA!")

    # Menu interativo
    print("\n" + "=" * 60)
    print("ESCOLHA UMA MISSÃO:")
    print("1 - Automação de arquivos")
    print("2 - Web scraping")
    print("3 - Envio de emails")
    print("4 - Sair")

    opcao = input("\n👉 Digite sua opção: ")

    if opcao == "1":
        cowsay.cow("Vamos organizar arquivos!")
    elif opcao == "2":
        cowsay.dragon("Web scraping é divertido!")
    elif opcao == "3":
        cowsay.cheese("Enviando emails automáticos!")
    else:
        cowsay.milk("Até a próxima missão!")

    print("\n✅ Script executado com sucesso!")

if __name__ == "__main__":
    main()
