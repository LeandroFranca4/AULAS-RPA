import pyautogui 
from time import sleep
import pyperclip


sleep(1)
pyautogui.hotkey('win','m')
sleep(1)
#abre o explorador
pyautogui.hotkey('win','e')
sleep(1)
#maximiza a tela
pyautogui.hotkey('win','up')
sleep(1)
#busca a pasta G1 e guarda os arquivos dos dia anterior no old
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(1)
pyautogui.typewrite('C:\Ativos_Cargas\G1')
pyautogui.press('enter')
sleep(1.5)

pyautogui.moveTo(426,444)

pyautogui.dragTo(425,235, button='left', duration=2)
sleep(2)

pyautogui.moveTo(465,301)
pyautogui.dragTo(414,216, button='left', duration=2)
sleep(3)
#fecha o explorador
pyautogui.hotkey('win','m')









#busca a pasta na barra de pesquisa

#abre a pasta arquivos sol
sleep(3)
pyautogui.moveTo(1234,38,duration=1)
pyautogui.doubleClick(1234,38)
sleep(2)
pyautogui.hotkey('win','up')

pyautogui.moveTo(607,186, duration=1)
pyautogui.rightClick(607,186)
sleep(1)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
sleep(2)
pyautogui.moveTo(491,187)
pyautogui.click(491,187)

sleep(1)
hoje=(pyautogui.locateCenterOnScreen('hoje.png'))
pyautogui.moveTo(hoje)
sleep(0.3)
pyautogui.click(hoje)









#copia todos os arquivos do dia, busca a pasta g1 e cola 
sleep(1)
pyautogui.press('down')
sleep(0.5)
pyautogui.press('enter')
sleep(1)
pyautogui.press('down')
sleep(1)
pyautogui.hotkey('ctrl','a')
sleep(0.5)
pyautogui.hotkey('ctrl','c')
sleep(3)
pyautogui.moveTo(857,154,duration=1)
pyautogui.click(857,154)
pyautogui.typewrite('C:\Ativos_Cargas\G1')
pyautogui.press('enter')
sleep(3)
pyautogui.moveTo(464,330,duration=1)
pyautogui.click(464,330)
pyautogui.hotkey('ctrl','v')
sleep(35)
pyautogui.click(372,433)
pyautogui.hotkey('win','m')
sleep(2)









#abre o explorador////NDG Import
pyautogui.hotkey('win','e')
sleep(1)
#maximiza a tela
pyautogui.hotkey('win','up')
sleep(1)
#busca a pasta G1
pyautogui.press('tab')
pyautogui.press('tab')
sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(1)
pyautogui.typewrite('C:\Ativos_Cargas\G1')
pyautogui.press('enter')
sleep(1.5)




pyautogui.moveTo(607,186, duration=1)
pyautogui.rightClick(607,186)
sleep(1)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
sleep(1)
pyautogui.moveTo(756,186,duration=1)
pyautogui.click(756,186)




sleep(2)
ex=(pyautogui.locateCenterOnScreen('ex.png'))
pyautogui.moveTo(ex)
sleep(0.3)
pyautogui.click(ex)
sleep(1)
pyautogui.press('down')
pyautogui.hotkey('enter')
sleep(7)

pyautogui.hotkey('win','up')
sleep(4)
pyautogui.press('right')
sleep(1)
pyautogui.press('right')
sleep(1)
pyautogui.press('right')

pyautogui.press('down')
sleep(2)
pyautogui.keyDown('shiftleft')
pyautogui.keyDown('shiftright')
pyautogui.keyDown('ctrlleft')
pyautogui.keyDown('ctrlright')
pyautogui.press('down')
pyautogui.keyUp('shiftleft')
pyautogui.keyUp('shiftright')
pyautogui.keyUp('ctrlleft')
pyautogui.keyUp('ctrlright')
sleep(2)
pyautogui.hotkey('ctrl', 'c')
sleep(1)
pyautogui.hotkey('win', 'm')
sleep(2)
for c in range (3):
    pyautogui.press('tab')

for c in range (5):
    pyautogui.press('right')

pyautogui.press('enter')

sleep(1)
for c in range (3):
    pyautogui.press('tab')
sleep(1)
pyautogui.press('right')      
sleep(1)  
pyautogui.press('enter')
sleep(1)
pyautogui.press('tab')
sleep(1)
pyautogui.hotkey('ctrl', 'v')

sleep(2)

pyautogui.moveTo(683,644,duration=0.5)
pyautogui.click(683,644) #aspas
sleep(8)
pyautogui.hotkey('win','m')














sleep(5)


#blocklist
pyautogui.hotkey('win','e')
sleep(1)
#maximiza a tela
pyautogui.hotkey('win','up')
sleep(1)
#busca a pasta G1
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(1)
pyautogui.typewrite('C:\Ativos_Cargas\G1')
pyautogui.press('enter')

sleep(1.5)





pyautogui.moveTo(607,186, duration=1)
pyautogui.rightClick(607,186)
sleep(1)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
sleep(1)

pyautogui.moveTo(420,186,duration=1)
pyautogui.click(420,186)
sleep(1)








ae=(pyautogui.locateCenterOnScreen('ea.png'))
pyautogui.moveTo(ae)
sleep(0.3)
pyautogui.click(ae)

sleep(0.5)
pyautogui.moveTo(325,215,duration=1)
pyautogui.click(325,215)
sleep(0.5)
pyautogui.press('f2')
pyautogui.press('left')

for c in range (9):
    pyautogui.press('right')
sleep(0.5)
for c in range(4):
    pyautogui.press('backspace')

pyautogui.press('enter')
sleep(1)

pyautogui.hotkey('ctrl', 'x')
sleep(1)
pyautogui.hotkey('win', 'm')
sleep(1)

sleep(2)

pyautogui.moveTo(1239,138,duration=1)
pyautogui.doubleClick(1239,138)




sleep(1)
pyautogui.hotkey('win','up')



sleep(3)
pyautogui.moveTo(509,360,duration=1)
pyautogui.click(509,360)

sleep(1)
pyautogui.hotkey('ctrl','v')
sleep(2)
pyautogui.hotkey('win','m')

sleep(4)















pyautogui.hotkey('win','e')
sleep(1)
#maximiza a tela
pyautogui.hotkey('win','up')
sleep(1)
#busca a pasta G1 e guarda os arquivos dos dia anterior no old
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(1)
pyautogui.typewrite('C:\Ativos_Cargas\G1')
pyautogui.press('enter')
sleep(1.5)

#busca a plan

pyautogui.moveTo(616,182,duration=1)
pyautogui.rightClick(616,182)
sleep(1)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')

pyautogui.moveTo(756,186,duration=1)
pyautogui.click(756,186)
sleep(2)
pyautogui.moveTo(767,211,duration=1)
pyautogui.click(767,211)

pyautogui.click(626,355)
sleep(1)
pyautogui.press('down')
pyautogui.hotkey('ctrl', 'c')
sleep(2)
pyautogui.hotkey('win','m')

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

#busca onde tem que anexar a planilha de pagamentos
plan=(pyautogui.locateCenterOnScreen('plan.png'))
pyautogui.moveTo(plan)
sleep(0.3)
pyautogui.click(plan)
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

sleep(60)












sleep(1)

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

#busca onde tem que anexar a planilha de pagamentos
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


pyautogui.moveTo(848,48,duration=1)
pyautogui.click(848,48)
sleep(1)
pyautogui.typewrite('C:\Ativos_Cargas\G1')
pyautogui.press('enter')

sleep(1.5)

pyautogui.moveTo(697,110,duration=1)
pyautogui.rightClick(697,110)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
sleep(3)

pyautogui.moveTo(671,110,duration=1)
pyautogui.click(671,110)
sleep(2)
#seleciona os arquivos de texto
pyautogui.click(678,155)
sleep(1)
pyautogui.click(656,379)

pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')

pyautogui.keyDown('shiftleft')
pyautogui.keyDown('shiftright')
pyautogui.keyDown('ctrlleft')
pyautogui.keyDown('ctrlright')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.keyUp('shiftleft')
pyautogui.keyUp('shiftright')
pyautogui.keyUp('ctrlleft')
pyautogui.keyUp('ctrlright')

pyautogui.press('enter')

sleep(1)

#avança
avancar=(pyautogui.locateCenterOnScreen('avancar.png'))
pyautogui.moveTo(avancar)
sleep(0.3)
pyautogui.click(avancar)
sleep(2)

#move para prosseguir
pyautogui.moveTo(898,311, duration=1)
#tirar aspas para funcionar
pyautogui.click(898,311)#aspas

sleep(8)




























