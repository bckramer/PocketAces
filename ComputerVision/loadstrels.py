from Utils import *
import cv2
from PIL import ImageGrab
import numpy as np

def loadPlayerStrels():
    strels = []

    two = cv2.imread('PlayerSE/2.PNG')
    two = binarizeAndErode(two, 2, 1, 210, False)
    strels.append(two)

    three = cv2.imread('PlayerSE/3.PNG')
    three = binarizeAndErode(three, 2, 1, 210, False)
    strels.append(three)

    four = cv2.imread('PlayerSE/4.PNG')
    four = binarizeAndErode(four, 2, 1, 210, False)
    strels.append(four)

    five = cv2.imread('PlayerSE/5.PNG')
    five = binarizeAndErode(five, 2, 1, 210, False)
    strels.append(five)

    six = cv2.imread('PlayerSE/6.PNG')
    six = binarizeAndErode(six, 2, 1, 210, False)
    strels.append(six)

    seven = cv2.imread('PlayerSE/7.PNG')
    seven = binarizeAndErode(seven, 2, 1, 210, False)
    strels.append(seven)

    eight = cv2.imread('PlayerSE/8.PNG')
    eight = binarizeAndErode(eight, 2, 1, 210, False)
    strels.append(eight)

    nine = cv2.imread('PlayerSE/9.PNG')
    nine = binarizeAndErode(nine, 2, 1, 210, False)
    strels.append(nine)

    ten = cv2.imread('PlayerSE/10.PNG')
    ten = binarizeAndErode(ten, 2, 1, 210, False)
    strels.append(ten)

    jack = cv2.imread('PlayerSE/J.PNG')
    jack = binarizeAndErode(jack, 2, 1, 210, False)
    strels.append(jack)

    queen = cv2.imread('PlayerSE/Q.PNG')
    queen = binarizeAndErode(queen, 2, 1, 210, False)
    strels.append(queen)

    king = cv2.imread('PlayerSE/K.PNG')
    king = binarizeAndErode(king, 2, 1, 210, False)
    strels.append(king)

    ace = cv2.imread('PlayerSE/A.PNG')
    ace = binarizeAndErode(ace, 2, 2, 210, False)
    strels.append(ace)

    return strels

def loadSuitStrels():
    suits = []

    spade = cv2.imread("PlayerSE/Spade.PNG")
    spade = binarizeAndErode(spade, 2, 1, 210, False)
    suits.append(spade)

    club = cv2.imread("PlayerSE/Club.PNG")
    club = binarizeAndErode(club, 2, 1, 210, False)
    suits.append(club)

    heart = cv2.imread("PlayerSE/Heart.PNG")
    heart = binarizeAndErode(heart, 2, 1, 210, False)
    suits.append(heart)

    diamond = cv2.imread("PlayerSE/Diamond.PNG")
    diamond = binarizeAndErode(diamond, 2, 1, 210, False)
    suits.append(diamond)

    return suits

def loadPotSizeStrels():
    nums = []

    zero = cv2.imread("PotSizeSE/0.PNG")
    zero = binarizeAndErode(zero, 2, 1, 150, True)
    nums.append(zero)

    one = cv2.imread("PotSizeSE/1.PNG")
    one = binarizeAndErode(one, 1, 1, 150, True)
    nums.append(one)

    two = cv2.imread("PotSizeSE/2.PNG")
    two = binarizeAndErode(two, 2, 1, 150, True)
    nums.append(two)

    three = cv2.imread("PotSizeSE/3.PNG")
    three = binarizeAndErode(three, 1, 1, 150, True)
    nums.append(three)

    four = cv2.imread("PotSizeSE/4.PNG")
    four = binarizeAndErode(four, 1, 1, 150, True)
    nums.append(four)

    five = cv2.imread("PotSizeSE/5.PNG")
    five = binarizeAndErode(five, 2, 1, 137, True)
    nums.append(five)

    six = cv2.imread("PotSizeSE/6.PNG")
    six = binarizeAndErode(six, 2, 1, 150, True)
    nums.append(six)

    seven = cv2.imread("PotSizeSE/7.PNG")
    seven = binarizeAndErode(seven, 1, 1, 150, True)
    nums.append(seven)

    eight = cv2.imread("PotSizeSE/8.PNG")
    eight = binarizeAndErode(eight, 1, 1, 150, True)
    nums.append(eight)

    nine = cv2.imread("PotSizeSE/9.PNG")
    nine = binarizeAndErode(nine, 1, 1, 150, True)
    nums.append(nine)

    return nums

def loadPublicStrels():
    strels = []

    two = cv2.imread('PublicCardsSE/2.PNG')
    two = binarizeAndErode(two, 1, 1, 210, False)
    strels.append(two)

    three = cv2.imread('PublicCardsSE/3.PNG')
    three = binarizeAndErode(three, 2, 1, 210, False)
    strels.append(three)

    four = cv2.imread('PublicCardsSE/4.PNG')
    four = binarizeAndErode(four, 1, 1, 210, False)
    strels.append(four)

    five = cv2.imread('PublicCardsSE/5.PNG')
    five = binarizeAndErode(five, 2, 1, 210, False)
    strels.append(five)

    six = cv2.imread('PublicCardsSE/6.PNG')
    six = binarizeAndErode(six, 3, 1, 210, False)
    strels.append(six)

    seven = cv2.imread('PublicCardsSE/7.PNG')
    seven = binarizeAndErode(seven, 2, 1, 210, False)
    strels.append(seven)

    eight = cv2.imread('PublicCardsSE/8.PNG')
    eight = binarizeAndErode(eight, 3, 1, 210, False)
    strels.append(eight)

    nine = cv2.imread('PublicCardsSE/9.PNG')
    nine = binarizeAndErode(nine, 5, 1, 210, False)
    strels.append(nine)

    ten = cv2.imread('PublicCardsSE/10.PNG')
    ten = binarizeAndErode(ten, 2, 1, 210, False)
    strels.append(ten)

    jack = cv2.imread('PublicCardsSE/J.PNG')
    jack = binarizeAndErode(jack, 3, 1, 210, False)
    strels.append(jack)

    queen = cv2.imread('PublicCardsSE/Q.PNG')
    queen = binarizeAndErode(queen, 2, 1, 210, False)
    strels.append(queen)

    king = cv2.imread('PublicCardsSE/K.PNG')
    king = binarizeAndErode(king, 2, 1, 210, False)
    strels.append(king)

    ace = cv2.imread('PublicCardsSE/A.PNG')
    ace = binarizeAndErode(ace, 2, 1, 210, False)
    strels.append(ace)

    return strels


def binarizeAndErode(image, size, numiter, lowerbinarybound, bitwise):
    kernel = np.ones((size, size), np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, lowerbinarybound, 255, cv2.THRESH_BINARY_INV)[1]
    if bitwise:
        image = cv2.bitwise_not(image)
    image = cv2.erode(image, kernel, iterations=numiter)
    return image