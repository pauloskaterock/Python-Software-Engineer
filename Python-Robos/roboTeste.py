
import time

# --- Documentação do Programa ---
# Este script usa a biblioteca pyautogui para automatizar interações
# de desktop, simulando um usuário movendo o mouse e digitando.

def automacao_teste():

    print("--- INÍCIO DA AUTOMAÇÃO ---")

    # 1. TEMPO DE ATRASO (CRUCIAL PARA RPA)
    # O time.sleep() é essencial para dar ao usuário tempo para mover
    # o mouse para fora da área de clique, ou para trocar de janela.
    # O robô irá esperar 5 segundos antes de começar.
    print("Aguardando 5 segundos. Por favor, posicione o cursor onde deseja digitar...")
    time.sleep(5)

    # 2. MOVER O MOUSE
    # pyautogui.moveTo(x, y, duration=tempo)
    # Move o cursor para as coordenadas (X, Y) na tela, levando 1 segundo.
    # ATENÇÃO: Os valores (X, Y) são relativos à sua tela. Você pode
    # precisar ajustá-los!
    # A função pyautogui.position() pode ajudar a encontrar coordenadas.
    # Exemplo: pyautogui.moveTo(100, 200, duration=1)



    # 3. DIGITAR NO TECLADO
    # pyautogui.write(texto)
    # Simula a digitação de cada caractere.
    frase_a_digitar = "Parceiro de Programacao diz: Automacao com Python eh incrivel!"
    print(f"Digitando: '{frase_a_digitar}'")

    pyautogui.write(frase_a_digitar, interval=0.1)

    # Adicionar um ENTER no final para, por exemplo, enviar um texto.
    pyautogui.press('enter')

    print("--- AUTOMAÇÃO CONCLUÍDA ---")

if __name__ == "__main__":
    try:
        automacao_teste()
    except Exception as e:
        print(f"Ocorreu um erro durante a automação: {e}")
