from itertools import count
import pyautogui
import time
time.sleep(3)

count = 0
while count<=100:
    pyautogui.typewrite("which phrases?")
    pyautogui.press("enter")
    