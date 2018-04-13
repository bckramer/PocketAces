import cv2
import numpy as np
# TODO - Refactor and add comments, Ben 3/25
# Case:            Error Output

def binarizeAndErode(image, size, numiter, lowerbinarybound, bitwise):
    kernel = np.ones((size, size), dtype='uint8')
    image = cv2.threshold(image, lowerbinarybound, 255, cv2.THRESH_BINARY_INV)[1]
    if bitwise:
        image = cv2.bitwise_not(image)
    if size != 0:
        image = cv2.erode(image, kernel, iterations=numiter)
    return image

def dilate(image, size, numiter):
    kernel = np.ones((size, size), np.uint8)
    image = cv2.dilate(image, kernel, iterations=numiter)
    return image

def addBlackBorder(image):
    row, col = image.shape[:2]
    bottom = image[row - 2:row, 0:col]

    bordersize = 40
    border = cv2.copyMakeBorder(image, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize,
                                borderType=cv2.BORDER_CONSTANT, value=cv2.BORDER_REPLICATE)
    return border

# Taken from https://stackoverflow.com/questions/36255654/how-to-add-border-around-an-image-in-opencv-python

# Simple debug function for making the values found human readable
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
        card1SuitName = "Spades"
    elif card1Suit == 1:
        card1SuitName = "Clubs"
    elif card1Suit == 2:
        card1SuitName = "Hearts"
    else:
        card1SuitName = "Diamonds"

    if card2Suit == 0:
        card2SuitName = "Spades"
    elif card2Suit == 1:
        card2SuitName = "Clubs"
    elif card2Suit == 2:
        card2SuitName = "Hearts"
    else:
        card2SuitName = "Diamonds"

    print ("Player Cards: " + card1Name + " of " + card1SuitName + " and " + card2Name + " of " + card2SuitName)

def printCard(cardValue, cardSuit):
    if cardValue == 11:
        cardName = "Jack"
    elif cardValue == 12:
        cardName = "Queen"
    elif cardValue == 13:
        cardName = "King"
    elif cardValue == 14:
        cardName = "Ace"
    else:
        cardName = str(cardValue)
    if cardSuit == 0:
        cardSuitName = "Spades"
    elif cardSuit == 1:
        cardSuitName = "Clubs"
    elif cardSuit == 2:
        cardSuitName = "Hearts"
    else:
        cardSuitName = "Diamonds"

    print(cardName + " of " + cardSuitName)

def getReadableCard(cardValue, cardSuit):
    if cardValue == 11:
        cardName = "Jack"
    elif cardValue == 12:
        cardName = "Queen"
    elif cardValue == 13:
        cardName = "King"
    elif cardValue == 14:
        cardName = "Ace"
    else:
        cardName = str(cardValue)
    if cardSuit == 0:
        cardSuitName = "Spades"
    elif cardSuit == 1:
        cardSuitName = "Clubs"
    elif cardSuit == 2:
        cardSuitName = "Hearts"
    else:
        cardSuitName = "Diamonds"

    return cardName + " of " + cardSuitName
