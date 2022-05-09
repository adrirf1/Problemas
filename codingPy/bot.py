from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#pyautogui.displayMousePosition()
for j in range(298,500,6):
    for i in range(608,810,5):
        pyautogui.click(i,j)
        time.sleep(2)