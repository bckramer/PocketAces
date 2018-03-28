import numpy as np
from PIL import ImageGrab
import cv2


#TODO - Refactor and add comments, Ben 3/25
def loadPlayerSE():
    strels = []

    two = cv2.imread('PlayerSE/2.PNG')
    two = binarizeAndErode(two)
    strels.append(two)

    three = cv2.imread('PlayerSE/3.PNG')
    three = binarizeAndErode(three)
    strels.append(three)

    four = cv2.imread('PlayerSE/4.PNG')
    four = binarizeAndErode(four)
    strels.append(four)

    five = cv2.imread('PlayerSE/5.PNG')
    five = binarizeAndErode(five)
    strels.append(five)

    six = cv2.imread('PlayerSE/6.PNG')
    six = binarizeAndErode(six)
    strels.append(six)

    seven = cv2.imread('PlayerSE/7.PNG')
    seven = binarizeAndErode(seven)
    strels.append(seven)

    eight = cv2.imread('PlayerSE/8.PNG')
    eight = binarizeAndErode(eight)
    strels.append(eight)

    nine = cv2.imread('PlayerSE/9.PNG')
    nine = binarizeAndErode(nine)
    strels.append(nine)

    ten = cv2.imread('PlayerSE/10.PNG')
    ten = binarizeAndErode(ten)
    strels.append(ten)

    jack = cv2.imread('PlayerSE/J.PNG')
    jack = binarizeAndErode(jack)
    strels.append(jack)

    queen = cv2.imread('PlayerSE/Q.PNG')
    queen = binarizeAndErode(queen)
    strels.append(queen)

    king = cv2.imread('PlayerSE/K.PNG')
    king = binarizeAndErode(king)
    strels.append(king)

    ace = cv2.imread('PlayerSE/A.PNG')
    ace = binarizeAndErode(ace)
    kernel = np.ones((2, 2), np.uint8)
    ace = cv2.erode(ace, kernel, iterations=1)
    strels.append(ace)

    return strels

def loadSuitStrels():
    suits = []

    club = cv2.imread("PlayerSE/Club.PNG")
    club = binarizeAndErode(club)
    suits.append(club)

    heart = cv2.imread("PlayerSE/Heart.PNG")
    heart = binarizeAndErode(heart)
    suits.append(heart)

    spade = cv2.imread("PlayerSE/Spade.PNG")
    spade = binarizeAndErode(spade)
    suits.append(spade)

    diamond = cv2.imread("PlayerSE/Diamond.PNG")
    diamond = binarizeAndErode(diamond)
    suits.append(diamond)

    return suits

def loadPotSizeStrels():
    nums = []

    zero = cv2.imread("PotSizeSE/0.PNG")
    zero = binarizeAndErode(zero)
    nums.append(zero)

    one = cv2.imread("PotSizeSE/1.PNG")
    one = binarizeAndErode(one)
    nums.append(one)

    two = cv2.imread("PotSizeSE/2.PNG")
    two = binarizeAndErode(two)
    nums.append(two)

    three = cv2.imread("PotSizeSE/3.PNG")
    three = binarizeAndErode(three)
    nums.append(three)

    four = cv2.imread("PotSizeSE/4.PNG")
    four = binarizeAndErode(four)
    nums.append(four)

    five = cv2.imread("PotSizeSE/5.PNG")
    five = binarizeAndErode(five)
    nums.append(five)

    six = cv2.imread("PotSizeSE/6.PNG")
    six = binarizeAndErode(six)
    nums.append(six)

    seven = cv2.imread("PotSizeSE/7.PNG")
    seven = binarizeAndErode(seven)
    nums.append(seven)

    eight = cv2.imread("PotSizeSE/8.PNG")
    eight = binarizeAndErode(eight)
    nums.append(eight)

    nine = cv2.imread("PotSizeSE/9.PNG")
    nine = binarizeAndErode(nine)
    nums.append(nine)

    return nums

def findElementInImage(image, structuringElements, cardValues):
    i = 0
    for strel in structuringElements:
        erosion = cv2.erode(image, strel, iterations=1)
        #J and 10 get mixed up a lot when looking for the value of a card.
        #This fixes that. Hopfully the root cause can be found, but for now, this works
        if (cardValues):
            row, col = erosion.shape
            erosion = erosion[0:col, 0:row - 20]
        im, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) == 1:
            return i
        i = i + 1
    return 0




def binarizeAndErode(image):
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY)[1]
    image = cv2.bitwise_not(image)
    image = cv2.erode(image, kernel, iterations=1)

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
