import numpy as np
from PIL import ImageGrab
import cv2
from ComputerVision.ScreenRead import readScreen
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()




while True:
    image = readScreen()
    if (image.all() != None):
        out.write(image)
    else:
        break