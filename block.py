import pyautogui
from time import sleep


pyautogui.moveTo(407,744,duration=1)
pyautogui.rightClick(407,744)
sleep(1)
pyautogui.click(328,400)
sleep(2)
pyautogui.hotkey('win','up')

sleep(3)
pyautogui.moveTo(509,360,duration=1)
pyautogui.click(509,360)

pyautogui.press('down')
pyautogui.press('enter')
sleep(3)


pyautogui.moveTo(468,185,duration=1)
pyautogui.rightClick(468,185)
sleep(1)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
sleep(1)


pyautogui.click(544,185)
sleep(2)

hoje=(pyautogui.locateCenterOnScreen('hoje.png'))
pyautogui.moveTo(hoje)
sleep(0.3)
pyautogui.click(hoje)


sleep(1)
pyautogui.press('down')
pyautogui.press('down')

pyautogui.hotkey('ctrl', 'c')

pyautogui.hotkey('win', 'm')



#abre o virtua digita usuário e senha
sleep(5)
pyautogui.moveTo(360,746, duration=1)
pyautogui.rightClick(360,746)
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('enter')
sleep(3)
pyautogui.moveTo(953,358, duration=1)
pyautogui.click(953,358)
pyautogui.typewrite('Leandro Henrique Franca')
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.moveTo(969,402, duration=1)
pyautogui.click(969,402)
pyautogui.typewrite('12345678')
pyautogui.moveTo(946,436, duration=1)
pyautogui.click(946,436)
sleep(13)

#busca o importador
importador=(pyautogui.locateCenterOnScreen('importador.png'))
pyautogui.moveTo(importador)
sleep(0.5)
pyautogui.click(importador)
sleep(2)

#busca avançar
avancar=(pyautogui.locateCenterOnScreen('avancar.png'))
pyautogui.moveTo(avancar)
sleep(0.5)
pyautogui.click(avancar)
sleep(1)

ativos=(pyautogui.locateCenterOnScreen('ativos.png'))
pyautogui.moveTo(ativos)
sleep(0.3)
pyautogui.click(ativos)
sleep(1)

#avança
avancar=(pyautogui.locateCenterOnScreen('avancar.png'))
pyautogui.moveTo(avancar)
sleep(0.3)
pyautogui.click(avancar)
sleep(1)

#busca selecionar aquivo e cola plan
selearquivo=(pyautogui.locateCenterOnScreen('selearquivo.png'))
pyautogui.moveTo(selearquivo)
sleep(0.3)
pyautogui.click(selearquivo)
sleep(2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(2)

#avança
avancar=(pyautogui.locateCenterOnScreen('avancar.png'))
pyautogui.moveTo(avancar)
sleep(0.3)
pyautogui.click(avancar)
sleep(2)

#move para prosseguir
pyautogui.moveTo(898,311, duration=1)
#tirar aspas para funcionar
pyautogui.click(898,311)

sleep(8)