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

def getAllValues(prevPot):
    screen_grab = ImageGrab.grab()
    cv_image = np.array(screen_grab, dtype='uint8')
    cv_image_grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    # All the binarizations of the board
    thresh, cv_image_bw = cv2.threshold(cv_image_grey, 200, 255, cv2.THRESH_BINARY_INV)
    thresh, cv_image_bw2 = cv2.threshold(cv_image_grey, 100, 255, cv2.THRESH_BINARY)
    thresh, cv_image_bw3 = cv2.threshold(cv_image_grey, 75, 255, cv2.THRESH_BINARY)
    # Image of the player cards
    cards = cv_image_bw[620:720, 1000:1100]
    # Image of the public cards, also known as the river
    publicCards = cv_image_bw[398:510, 912:1400]
    # Image of the public pot size
    potSize = cv_image_bw2[533:570, 780:950]
    # Image of the players pot size
    playerChips = cv_image_bw3[810:838, 1000:1170]
    y, x = playerChips.shape[:2]
    playerChips = playerChips[0:y - 2, 0:x]
    # Anchor for checking if there is only one card present
    oneCardCheck = cv_image_bw2[770:780, 1142:1152]
    # If there is only one card, set all card values to 0
    im, contours, hierarchy = cv2.findContours(oneCardCheck, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        card1Value = 0
        card2Value = 0
        card1Suit = 0
        card2Suit = 0
    else:
        card1Value, card2Value = findCards(cards)
        card1Suit, card2Suit = findSuits(cards)
    # Find the value of the pot size
    potSize = findChipSize(potSize, 1, 2)
    if potSize == -1:
        potSize = 0
    # Find the players pot size
    playerPot = findChipSize(playerChips, chipCountStrels, 2)
    # Find the values of the public cards and their suits
    publicCardValues, publicCardSuits = findPublicCards(publicCards)
    # Need to be broken down for the neural network
    publicCardValue0 = publicCardValues[0]
    publicCardValue1 = publicCardValues[1]
    publicCardValue2 = publicCardValues[2]
    publicCardValue3 = publicCardValues[3]
    publicCardValue4 = publicCardValues[4]
    # Suits needs to be one value for the network
    stringSuits = ""
    for suit in publicCardSuits:
        if suit == -1:
            suit = 0
        stringSuits = stringSuits + str(suit)
    intSuits = int(stringSuits)
    # Calculate the size of the opponents call
    callSize = int(potSize) - int(prevPot)
    # Create the array of all the values found
    allValues = np.array([card1Value, card1Suit, card2Value, card2Suit, publicCardValue0, publicCardValue1, publicCardValue2, publicCardValue3, publicCardValue4, intSuits, potSize, playerPot, callSize])
    # Convert all values to integers
    allValues = allValues.astype(np.int)

    return allValues

def buttonsAvailable():
    screen_grab = ImageGrab.grab()
    cv_image = np.array(screen_grab, dtype='uint8')
    cv_image_grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    thresh, cv_image_bw = cv2.threshold(cv_image_grey, 220, 255, cv2.THRESH_BINARY)
    thresh, cv_image_bw2 = cv2.threshold(cv_image_grey, 100, 255, cv2.THRESH_BINARY)

    buttons = cv_image_bw[840:900, 800:1420]
    dealButton = cv_image_bw[840:900, 800:888]
    foldButton = cv_image_bw[840:900, 888:970]
    checkCallButton = cv_image_bw[840:900, 1000:1080]
    raiseButton = cv_image_bw[840:900, 1090:1170]
    allInButton = cv_image_bw[840:900, 1310:1400]
    continueButton = cv_image_bw[532:560, 950:1200]
    playAgainButton = cv_image_bw2[365:370, 1070:1080]

    dealButtonOn = False
    foldButtonOn = False
    checkCallButtonOn = False
    raiseButtonOn = False
    allInButtonOn = False
    continueButtonOn = False
    playAgainButtonOn = False

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
    im, contours, hierarchy = cv2.findContours(playAgainButton, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        playAgainButtonOn = True



    return dealButtonOn, foldButtonOn, checkCallButtonOn, raiseButtonOn, allInButtonOn, continueButtonOn, playAgainButtonOn