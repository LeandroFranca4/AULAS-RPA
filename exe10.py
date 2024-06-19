import webbrowser
import pyautogui
from time import sleep

#abrir uma aba no navegador existente
'''webbrowser.open('instagram.com/leandrofranca.4/?next=%2F')'''

#abrir uma nova aba em um navegador existente ou criar outro
'''webbrowser.open_new_tab('instagram.com/leandrofranca.4/?next=%2F')'''

#criar e abrir uma nova janela do zero
webbrowser.open_new('https://cursoautomacao.netlify.app/')
pyautogui.moveTo(2721,255, duration=3)
pyautogui.click(2721,255)
pyautogui.moveTo(2528,548, duration=2)
pyautogui.click(2528,548)
pyautogui.typewrite('Leandro Henrique França de Freitas')
pyautogui.moveTo(2426,595, duration=2)
pyautogui.click(2426,595)
pyautogui.moveTo(2217,208, duration=2)
pyautogui.click(2217,208)
pyautogui.scroll(1500)
pyautogui.scroll(-2000)
pyautogui.moveTo(1540,433, duration=2)
pyautogui.click(1540,433)
pyautogui.moveTo(1726,435, duration=2)
pyautogui.click(1726,435)
sleep(1)
pyautogui.alert(text='TERMINOU', title='Automação', button='OK')

