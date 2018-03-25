import numpy as np
from PIL import ImageGrab
import cv2
from ScreenRead import read_screen
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

while (True) :
    read_screen()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()