import time

import pyautogui


time.sleep(15)
for i in range(1000):
    pyautogui.write("I love you")
    pyautogui.press("Enter")
    i += 1

