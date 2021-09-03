import time
import random
import os
import pyautogui
def Format():
    os.system("open /System/Applications/Messages.app")
    time.sleep(1)
    pyautogui.click(y=500, x=300)
    pyautogui.typewrite("14083101955")
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.click(y=763, x=500)
def Brain():
    for x in range(0, 10):
        time.sleep(1)
        a = ["test this was sent by bot", "jhqwsgfbsjh", "hihihhih"]
        x = random.choice(a)
        os.system("open /System/Applications/Messages.app")
        time.sleep(3)
        pyautogui.typewrite(x)
        pyautogui.press("enter")
Format()
Brain()


