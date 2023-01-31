import pyautogui
import keyboard
import time

time.sleep(10)

file = open(r"spam.txt", "r")
fileread = file.read()

print(fileread)

while keyboard.is_pressed("q") == False:
    pyautogui.typewrite(fileread)
    pyautogui.press("ENTER")

