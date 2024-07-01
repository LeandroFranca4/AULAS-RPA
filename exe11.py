import pyautogui 
import webbrowser
import pyperclip
from time import sleep

def email(email):
    pyperclip.copy(email)
    pyautogui.hotkey('ctrl', 'v')

def senha(senha):
     pyperclip.copy(senha)
     pyautogui.hotkey('ctrl', 'v')


webbrowser.open_new('https://www.instagram.com/')
sleep(8)

pyautogui.moveTo(841,291, duration=1)
pyautogui.click(841,291)
email('leandro24798@gmail.com')
pyautogui.moveTo(801,333, duration=1)
pyautogui.click(801,333)
email('Le040404!@#$')
pyautogui.moveTo(817,380, duration=1)
pyautogui.click(817,380)
sleep(10)
pyautogui.moveTo(798,451, duration=1)
pyautogui.click(798,451)
sleep(2)
pyautogui.click(x=98, y=273, duration=2)
pyautogui.moveTo(135,203, duration=1)
pyautogui.click(135,203, duration=2)
pyautogui.typewrite('leandrofranca')
sleep(5)
pyautogui.moveTo(161,261, duration=1)
pyautogui.click(161,261)
sleep(2)
pyautogui.moveTo(469,624, duration=1)
pyautogui.click(469,624)

sleep(5)
coracao = pyautogui.locateCenterOnScreen('coracao.PNG')
coration = pyautogui.locateCenterOnScreen('coration.PNG')

sleep(2)



if coration == None:
    pyautogui.moveTo(x=750, y=571, duration=1)
    pyautogui.click(x=750, y=571)
    pyautogui.moveTo(851,675, duration=1)
    pyautogui.click(851,675)
    pyautogui.typewrite('HOAAAAAAAAAAAAAAAAAAAAAA///')
    pyautogui.press('enter')

if coracao is not None:
    print('não achou')




'''left=23, top=259, width=151, height=29'''
