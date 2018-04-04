import numpy as np
from Utils import *
from findcontours import *
from loadstrels import *
from PIL import ImageGrab
import cv2
import time
# VERY IMPORTANT: Without it, the entire screen will not be captured
from ctypes import windll

user32 = windll.user32
user32.SetProcessDPIAware()
valueStrels = loadPlayerStrels()
suitStrels = loadSuitStrels()
potSizeStrels = loadPotSizeStrels()
publicstrels = loadPublicStrels()
chipCountStrels = loadChipCountStrels()

# TODO - Refactor and add comments, Ben 3/25
# TODO - System doesn't work if there is only one card, fix, Ben3/28

# Finds the players current suit
def findSuits(cardsImage):
    card1Suit = cardsImage[50:100, 10:50]
    card2Suit = cardsImage[58:100, 48:80]
    card1 = findElementInImage(card1Suit, suitStrels, False)
    card2 = findElementInImage(card2Suit, suitStrels, False)

    return card1, card2

# Finds the cards in the users hand
def findCards(cardsImage):
    kernel = np.ones((1, 1), np.uint8)
    card1Value = cardsImage[8:50, 12:50]
    card1Value = cv2.erode(card1Value, kernel, iterations=1)
    card2Value = cardsImage[20:58, 48:80]
    card2Value = cv2.erode(card2Value, kernel, iterations=1)

    card1 = findElementInImage(card1Value, valueStrels, True) + 2
    card2 = findElementInImage(card2Value, valueStrels, True) + 2

    return card1, card2

def findChipSize(chipSizeImage, strels, size):
    kernel = np.ones((size, size), dtype='uint8')
    chipSizeImage = cv2.dilate(chipSizeImage, kernel, iterations=1)
    return determinePotSize(chipSizeImage, strels, loadPlayerDollar())

def findPublicCards(publiccards):
    height, width = publiccards.shape

    card1 = publiccards[0:height - (height / 2) - 20, 0:(width/5) - 68]
    card2 = publiccards[0:height - (height / 2) - 20, width/5 + 5:(width / 5) * 2 - 63]
    card3 = publiccards[0:height - (height / 2) - 20, (width / 5) * 2 + 10:(width / 5) * 3 - 62]
    card4 = publiccards[0:height - (height / 2) - 20, (width / 5) * 3 + 12:(width / 5) * 4 - 56]
    card5 = publiccards[0:height - (height / 2) - 20, (width / 5) * 4 + 20:(width / 5) * 5 - 50]
    card1val = findElementInImage(card1, publicstrels, True) + 2
    card2val = findElementInImage(card2, publicstrels, True) + 2
    card3val = findElementInImage(card3, publicstrels, True) + 2
    card4val = findElementInImage(card4, publicstrels, True) + 2
    card5val = findElementInImage(card5, publicstrels, True) + 2

    return card1val, card2val, card3val, card4val, card5val
