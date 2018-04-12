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
user32 = windll.user32
user32.SetProcessDPIAware()

def getAllValues():
    screen_grab = ImageGrab.grab()
    cv_image = np.array(screen_grab, dtype='uint8')
    cv_image_grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    thresh, cv_image_bw = cv2.threshold(cv_image_grey, 200, 255, cv2.THRESH_BINARY_INV)
    cards = cv_image_bw[620:720, 1000:1100]
    publicCards = cv_image_bw[398:510, 912:1400]

    thresh, cv_image_bw2 = cv2.threshold(cv_image_grey, 100, 255, cv2.THRESH_BINARY)
    thresh, cv_image_bw3 = cv2.threshold(cv_image_grey, 75, 255, cv2.THRESH_BINARY)
    thresh, cv_image_bw4 = cv2.threshold(cv_image_grey, 220, 255, cv2.THRESH_BINARY)


    potSize = cv_image_bw2[533:570, 800:950]
    w, h = cv_image_bw.shape[:2]
    playerChips = cv_image_bw3[810:838, 1000:1170]
    y, x = playerChips.shape[:2]
    playerChips = playerChips[0:y - 2, 0:x]

    # Use to get pot size
    # Use to get player chips

    card1Value, card2Value = findCards(cards)
    card1Suit, card2Suit = findSuits(cards)
    potSize = findChipSize(potSize, 1, 2)
    publicCardValues, publicCardSuits = findPublicCards(publicCards)
    playerPot = findChipSize(playerChips, chipCountStrels, 2)

    publicCardValue0 = publicCardValues[0]
    publicCardValue1 = publicCardValues[1]
    publicCardValue2 = publicCardValues[2]
    publicCardValue3 = publicCardValues[3]
    publicCardValue4 = publicCardValues[4]

    stringSuits = ""

    for suit in publicCardSuits:
        stringSuits = stringSuits + str(suit)

    intSuits = int(stringSuits)

    print (intSuits)

    return np.array([card1Value, card1Suit, card2Value, card2Suit, publicCardValue0, publicCardValue1, publicCardValue2, publicCardValue3, publicCardValue4, intSuits, potSize, playerPot])

def buttonsAvailable():
    screen_grab = ImageGrab.grab()
    cv_image = np.array(screen_grab, dtype='uint8')
    cv_image_grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    thresh, cv_image_bw = cv2.threshold(cv_image_grey, 220, 255, cv2.THRESH_BINARY)

    buttons = cv_image_bw[840:900, 800:1420]
    dealButton = cv_image_bw[840:900, 800:888]
    foldButton = cv_image_bw[840:900, 888:970]
    checkCallButton = cv_image_bw[840:900, 1000:1080]
    raiseButton = cv_image_bw[840:900, 1090:1170]
    allInButton = cv_image_bw[840:900, 1310:1400]
    continueButton = cv_image_bw[532:580, 950:1200]

    dealButtonOn = False
    foldButtonOn = False
    checkCallButtonOn = False
    raiseButtonOn = False
    allInButtonOn = False
    continueButtonOn = False

    im, contours, hierarchy = cv2.findContours(dealButton, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        dealButtonOn = True
    im, contours, hierarchy = cv2.findContours(foldButton, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        foldButtonOn = True
    im, contours, hierarchy = cv2.findContours(checkCallButton, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        checkCallButtonOn = True
    im, contours, hierarchy = cv2.findContours(raiseButton, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        raiseButtonOn = True
    im, contours, hierarchy = cv2.findContours(allInButton, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        allInButtonOn = True
    im, contours, hierarchy = cv2.findContours(continueButton, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        continueButtonOn = True


    return dealButtonOn, foldButtonOn, checkCallButtonOn, raiseButtonOn, allInButtonOn, continueButtonOn