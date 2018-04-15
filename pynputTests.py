from pynput.mouse import Button, Controller

from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()
mouse = Controller()

while True:

    print (mouse.position)