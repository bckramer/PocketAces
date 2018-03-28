#Below is a simple way to grab the entire screen in 1920x1080,
#but it should work in other resolutions.
import numpy as np
from Utils import *
from PIL import ImageGrab
import cv2
import time
#VERY IMPORTANT: Without it, the entire screen will not be captured
from ctypes import windll

user32 = windll.user32
user32.SetProcessDPIAware()
valueStrels = loadPlayerSE()
suitStrels = loadSuitStrels()

#TODO - Refactor and add comments, Ben 3/25
#TODO - System doesn't work if there is only one card, fix, Ben3/28
#Finds the players current suit
def findSuit(cardsImage):
    card1 = 0
    card2 = 0
    card1Suit = cv2.bitwise_not(cardsImage[50:100, 10:50])
    card2Suit = cv2.bitwise_not(cardsImage[58:100, 48:80])
    i = 0
    card1 = findElementInImage(card1Suit, suitStrels, False)
    card2 = findElementInImage(card2Suit, suitStrels, False)

    return card1, card2

#Finds the cards in the users hand
def findCards(cardsImage):
    kernel = np.ones((1, 1), np.uint8)
    card1Value = cv2.bitwise_not(cardsImage[8:50, 12:50])
    card1Value = cv2.erode(card1Value, kernel, iterations=1)
    card2Value = cv2.bitwise_not(cardsImage[20:58, 48:80])
    card2Value = cv2.erode(card2Value, kernel, iterations=1)
    card1 = 0
    card2 = 0
    i = 0
    card1 = findElementInImage(card1Value, valueStrels, True) + 2
    card2 = findElementInImage(card2Value, valueStrels, True) + 2

    return card1, card2

while True:
    screen_grab = ImageGrab.grab()
    cv_image = np.array(screen_grab, dtype='uint8')
    cv_image_grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    thresh, cv_image_bw = cv2.threshold(cv_image_grey, 200, 255, cv2.THRESH_BINARY)
    cards = cv_image_bw[620:795, 1000:1200]
    resize = cv2.resize(cv_image_bw, (1280, 720))
    card1Value, card2Value = findCards(cards)
    card1Suit, card2Suit = findSuit(cards)
    printResult(card1Value, card2Value, card1Suit, card2Suit)
    time.sleep(1)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

