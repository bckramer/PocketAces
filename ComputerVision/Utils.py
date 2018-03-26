import numpy as np
from PIL import ImageGrab
import cv2

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

def binarizeAndErode(image):
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY)[1]
    image = cv2.bitwise_not(image)
    image = cv2.erode(image, kernel, iterations=1)

    return image
