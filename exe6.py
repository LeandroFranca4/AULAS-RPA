import pyautogui


'''email = pyautogui.prompt(text='digite seu log', title='informações obrigatórias')
print(f'vc figitou {email}')'''

'''pyautogui.alert(text="alooo", title='Automação de Login', button='ok')'''

resposta = pyautogui.confirm(text='continuar perdendo ou mudar de vida?', buttons=['sim', 'não', 'já é nosso carai'])
print(f'a resposta foi {resposta}')