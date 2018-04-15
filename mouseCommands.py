from pynput.mouse import Button, Controller
import time
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

mouse = Controller()
time.sleep(1)

def playAgain():
    mouse.position = (977, 857)
    mouse.press(Button.left)
    mouse.release(Button.left)