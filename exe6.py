import pyautogui
from time import sleep


email = pyautogui.prompt(text='digite seu log', title='informações obrigatórias')
print(f'vc figitou {email}')

pyautogui.alert(text="alooo", title='Automação de Login', button='ok')

resposta = pyautogui.confirm(text='continuar perdendo ou mudar de vida?', buttons=['sim', 'não', 'já é nosso carai'])
print(f'a resposta foi {resposta}')

'''pyautogui.hotkey('win', 'e')                    
sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')      
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
sleep(1)
pyautogui.press('tab')
pyautogui.press('right')
sleep(0.5)
pyautogui.press('right')
sleep(1)
pyautogui.press('enter')'''




  







