import pyautogui
import pyperclip

'''for c in range (10):
    pyautogui.moveTo(1942,692, duration=0.01)
    pyautogui.click()
    pyautogui.typewrite('8===3 trava zap')
    pyautogui.moveTo(2692,695, duration=0.01)
    pyautogui.click()'''

'''def frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')


pyautogui.moveTo(1802,280, duration=1)
pyautogui.click()
frase('çáááá')'''
    

def pinto(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

pyautogui.moveTo(1802,280, duration=1)
pyautogui.click()
pinto('pintolaço')



