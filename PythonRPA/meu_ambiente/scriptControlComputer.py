import pyautogui as posicaoMouse

posicaoMouse.sleep(4)
print(posicaoMouse.position())

# # moviemntação do mouse
posicaoMouse.moveTo(x=320, y=240)

posicaoMouse.click(x=320, y=240)

# # posicaoMouse.press('win')


posicaoMouse.typewrite('bloco de notas')
# # posicaoMouse.write('bloco de notas')

# posicaoMouse.sleep(4)
# posicaoMouse.doubleClick(x=1010, y=1047)
