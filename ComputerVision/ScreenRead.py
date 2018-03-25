# Below is a simple way to grab the entire screen in 1920x1080,
# but it should work in other resolutions.
import numpy as np
from PIL import ImageGrab
import cv2
# VERY IMPORTANT: Without it, the entire screen will not be captured
from ctypes import windll

user32 = windll.user32
user32.SetProcessDPIAware()


def read_screen():
    screen_grab = ImageGrab.grab()
    # Converted to an array OpenCV can use.
    cv_image = np.array(screen_grab, dtype='uint8')
    # cv2.imshow('window', printscreen_numpy)
    cv_image_grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    unimportant, cv_image_bw = cv2.threshold(cv_image_grey, 80, 100, cv2.THRESH_BINARY)
    resize = cv2.resize(cv_image_bw, (250, 175))

    cv2.imshow("Window", cv_image_bw)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
