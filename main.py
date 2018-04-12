# Below is a simple way to grab the entire screen in 1920x1080,
# but it should work in other resolutions.
import numpy as np
from Utils import *
from findcontours import *
from loadstrels import *
from findvalues import *
from PIL import ImageGrab
from ScreenRead import *
import cv2
import time
# VERY IMPORTANT: Without it, the entire screen will not be captured
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

while True:

    card1Value, card1Suit, card2Value, publicCardValues, publicCardSuits, card2Suit, potSize, playerPot = getAllValues()

    dealButtonOn, foldButtonOn, checkCallButtonOn, raiseButtonOn, allInButtonOn = buttonsAvailable()
