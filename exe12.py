import pyautogui
from time import sleep


sleep(5)
importador=(pyautogui.locateCenterOnScreen('importador.png'))

pyautogui.moveTo(importador, duration=2)
