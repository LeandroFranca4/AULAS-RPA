import pyautogui
from time import sleep


pyautogui.keyDown('shiftleft')
pyautogui.keyDown('shiftright')

pyautogui.keyDown('ctrlleft')
pyautogui.keyDown('ctrlright')
pyautogui.press('down')
pyautogui.keyUp('shiftleft')
pyautogui.keyUp('shiftright')
pyautogui.keyUp('ctrlleft')
pyautogui.keyUp('ctrlright')