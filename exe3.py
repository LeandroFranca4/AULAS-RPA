import pyautogui
from time import sleep

pyautogui.moveTo(2078,408, duration=1)
for c in range(100):
    pyautogui.scroll(-1500)
    sleep(1)


