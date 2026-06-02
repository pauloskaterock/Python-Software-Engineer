import pyautogui
import subprocess
import time

def abrir_bloco_de_notas():
    subprocess.Popen('notepad.exe')
    time.sleep(5)  # Aguarda 2 segundos para o Bloco de Notas abrir

def escrever_no_bloco_de_notas(texto):
    # Move o cursor do mouse para a posição do Bloco de Notas
    pyautogui.click(x=100, y=100)  # Ajuste as coordenadas conforme necessário

    # Digita o texto
    pyautogui.write(texto, interval=0.1)
    pyautogui.press('enter')  # Pressiona Enter

if __name__ == "__main__":
    abrir_bloco_de_notas()
    texto_para_escrever = "Corinthians Maior de todos"
    escrever_no_bloco_de_notas(texto_para_escrever)
