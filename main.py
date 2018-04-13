# Below is a simple way to grab the entire screen in 1920x1080,
# but it should work in other resolutions.
from ScreenRead import *
from run_this import *
import cv2
import time
# VERY IMPORTANT: Without it, the entire screen will not be captured
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

while True:

    # publicCardValue and publicCardSuits are arrays of ints, everything else is an int
    #card1Value, card1Suit, card2Value, publicCardValues, publicCardSuits, card2Suit, potSize, playerPot = getAllValues()


    # All booleans
    dealButtonOn, foldButtonOn, checkCallButtonOn, raiseButtonOn, allInButtonOn, continueButtonOn = buttonsAvailable()
