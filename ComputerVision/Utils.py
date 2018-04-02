import cv2
import numpy as np
# TODO - Refactor and add comments, Ben 3/25
# Case:            Error Output

def binarizeAndErode(image, size, numiter, lowerbinarybound, bitwise):
    kernel = np.ones((size, size), np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, lowerbinarybound, 255, cv2.THRESH_BINARY_INV)[1]
    if bitwise:
        image = cv2.bitwise_not(image)
    image = cv2.erode(image, kernel, iterations=numiter)
    return image

def dilate(image, size, numiter):
    kernel = np.ones((size, size), np.uint8)
    image = cv2.dilate(image, kernel, iterations=numiter)
    return image

#Simple debug function for making the values found human readable
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

    print "You have a " + card1Name + " of " + card1SuitName
    print "You have a " + card2Name + " of " + card2SuitName
