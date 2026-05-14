import pyautogui as openGoogle

openGoogle.sleep(4)

# print(openGoogle.position())

print(f"Posição atual do Mouse:{openGoogle.position()}")

openGoogle.click(x=1010, y=1047)
openGoogle.sleep(3)

print("-------------Digitando URL---------------")
openGoogle.typewrite('https://www.google.com/')
openGoogle.sleep(6)
openGoogle.press('enter')
openGoogle.sleep(3)

print(f"Posição atual do google:{openGoogle.position()}")
print(openGoogle.position())

# openGoogle.click(x=744, y=512)
openGoogle.sleep(3)

print("-------------Busca Tharsher Magzine---------------")
openGoogle.typewrite('Thrasher Magazine')
openGoogle.sleep(6)
openGoogle.press('enter')
