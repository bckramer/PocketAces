# Below is a simple way to grab the entire screen in 1920x1080,
# but it should work in other resolutions.
import numpy as np
from Utils import *
from findcontours import *
from loadstrels import *
from PIL import ImageGrab
from findvalues import *
import cv2
import time
# VERY IMPORTANT: Without it, the entire screen will not be captured
from ctypes import windll

while True:
    screen_grab = ImageGrab.grab()

    cv_image = np.array(screen_grab, dtype='uint8')
    cv_image_grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    thresh, cv_image_bw = cv2.threshold(cv_image_grey, 200, 255, cv2.THRESH_BINARY_INV)
    cards = cv_image_bw[620:720, 1000:1100]
    publicCards = cv_image_bw[398:510, 912:1400]

    thresh, cv_image_bw2 = cv2.threshold(cv_image_grey, 100, 255, cv2.THRESH_BINARY)
    thresh, cv_image_bw3 = cv2.threshold(cv_image_grey, 75, 255, cv2.THRESH_BINARY)

    potSize = cv_image_bw2[533:570, 800:950]
    playerChips = cv_image_bw3[810:838, 1000:1170]
    y, x = playerChips.shape[:2]
    playerChips = playerChips[0:y - 2, 0:x]

    # Use to get pot size
    print findChipSize(potSize, potSizeStrels, 2)
    # Use to get player chips
    # findChipSize(playerChips, chipCountStrels, 2)

    card1Value, card2Value = findCards(cards)
    card1Suit, card2Suit = findSuits(cards)
    printResult(card1Value, card2Value, card1Suit, card2Suit)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

