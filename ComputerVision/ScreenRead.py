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
#Finds the players current suit
def findSuit(cardsImage):
    card1 = 0
    card2 = 0
    card1Suit = cv2.bitwise_not(cardsImage[50:100, 10:50])
    card2Suit = cv2.bitwise_not(cardsImage[58:100, 48:80])
    i = 0
    for strel in suitStrels:
        erosion = cv2.erode(card1Suit, strel, iterations=1)
        im, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) == 1:
            card1 = i
        i = i + 1
    i = 0
    for strel in suitStrels:
        erosion = cv2.erode(card2Suit, strel, iterations=1)
        im, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 1:
            card2 = i
        i = i + 1

    return card1, card2

#Finds the cards in the users hand
def findCards(cardsImage):
    kernel = np.ones((1, 1), np.uint8)
    card1Value = cv2.bitwise_not(cardsImage[8:50, 12:50])
    card1Value = cv2.erode(card1Value, kernel, iterations=1)
    card2Value = cv2.bitwise_not(cardsImage[20:58, 48:80])
    card2Value = cv2.erode(card2Value, kernel, iterations=1)
    cardImages = []
    cardImages.append(card1Value)
    cardImages.append(card2Value)
    cards = []
    card1 = 0
    card2 = 0
    cards.append(card1)
    cards.append(card2)
    i = 0
    for card in cardImages:
        j = 2
        for strel in valueStrels:
            erosion = cv2.erode(card, strel, iterations = 1)
            row, col = erosion.shape
            erosion = erosion[0:col, 0:row - 20]
            im, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE,
                                                        cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) == 1:
                cards[i] = j
            j = j + 1
        i = i + 1

    return cards[0], cards[1]

def printResult(card1Value, card2Value, card1Suit, card2Suit):
    if card1Value == 11:
        card1Name = "Jack"
    elif card1Value == 12:
        card1Name = "Queen"
    elif card1Value == 13:
        card1Name = "King"
    elif card1Value == 14:
        card1Name = "Ace"
    else:
        card1Name = str(card1Value)

    if card2Value == 11:
        card2Name = "Jack"
    elif card2Value == 12:
        card2Name = "Queen"
    elif card2Value == 13:
        card2Name = "King"
    elif card2Value == 14:
        card2Name = "Ace"
    else:
        card2Name = str(card2Value)

    if card1Suit == 0:
        card1SuitName = "Clubs"
    elif card1Suit == 1:
        card1SuitName = "Hearts"
    elif card1Suit == 2:
        card1SuitName = "Spades"
    else:
        card1SuitName = "Diamonds"

    if card2Suit == 0:
        card2SuitName = "Clubs"
    elif card2Suit == 1:
        card2SuitName = "Hearts"
    elif card2Suit == 2:
        card2SuitName = "Spades"
    else:
        card2SuitName = "Diamonds"

    print "You have a " + card1Name + " of " + card1SuitName
    print "You have a " + card2Name + " of " + card2SuitName



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

