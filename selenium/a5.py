import pyautogui
from time import sleep


pyautogui.moveTo(1151,703)
pyautogui.click(1151,703)
for c in range(500):
    pyautogui.typewrite('você gosta do pablo do arrocha?')
    sleep(0.5)
    pyautogui.click(1326,689)