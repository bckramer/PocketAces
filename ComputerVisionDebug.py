# Run this script to verify information about the game
# is being read correctly
import numpy as np
from Utils import *
from findcontours import *
from loadstrels import *
from PIL import ImageGrab
from findvalues import *
from ScreenRead import *
import cv2
import time
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

newPotSizeStrels = loadPotSizeStrels()
callSize = 0
prevPotSize = 0
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
    playAgain = cv_image_bw2[365:370, 1070:1080]
    y, x = playerChips.shape[:2]
    playerChips = playerChips[0:y - 2, 0:x]

    # Use to get pot size
    # Use to get player chips

    card1Value, card2Value = findCards(cards)
    card1Suit, card2Suit = findSuits(cards)
    printResult(card1Value, card2Value, card1Suit, card2Suit)
    potSize = findChipSize(potSize, 1, 2)
    callSize = int(potSize) - prevPotSize
    prevPotSize = int(potSize)
    print("Call size: " + str(callSize))
    playerPot = findChipSize(playerChips, 0, 2)
    values = getAllValues(0)
    buttons = buttonsAvailable()
    print("Pot size: " + str(potSize) + " Player Pot: " + str(playerPot))
    cardValues, cardSuits = findPublicCards(publicCards)
    i = 0
    for card in cardValues:
        printCard(int(card), int(cardSuits[i]))
        i = i + 1
    time.sleep(2)
    print ("")

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

