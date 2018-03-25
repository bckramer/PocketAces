# Below is a simple way to grab the entire screen in 1920x1080,
# but it should work in other resolutions.
import numpy as np
from PIL import ImageGrab
import cv2
# VERY IMPORTANT: Without it, the entire screen will not be captured
from ctypes import windll

user32 = windll.user32
user32.SetProcessDPIAware()


while True:
    screen_grab = ImageGrab.grab()
    # Converted to an array OpenCV can use.
    cv_image = np.array(screen_grab, dtype='uint8')
    # cv2.imshow('window', printscreen_numpy)
    cv_image_grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    thresh, cv_image_bw = cv2.threshold(cv_image_grey, 200, 255, cv2.THRESH_BINARY)
    cards = cv_image_bw[620:795, 1000:1200]
    resize = cv2.resize(cv_image_bw, (1280, 720))
    cv2.imshow("Window", resize)
    cv2.imshow("Cards", cards)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

#Finds the cards in the users hand
#def findCards(cards):