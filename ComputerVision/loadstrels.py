from Utils import *
import cv2

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

    dollar = cv2.imread("PotSizeSE/$.PNG")
    dollar = binarizeAndErode(dollar, 2, 1, 150, True)
    nums.append(dollar)

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

def loadChipCountStrels():
    nums = []

    dollar = cv2.imread("PotSizeSE/$.PNG")
    dollar = binarizeAndErode(dollar, 2, 1, 150, True)
    nums.append(dollar)

    zero = cv2.imread("ChipSE/0.PNG")
    zero = cv2.cvtColor(zero, cv2.COLOR_BGR2GRAY)
    zero = cv2.threshold(zero, 150, 255, cv2.THRESH_BINARY_INV)[1]
    nums.append(zero)

    one = cv2.imread("ChipSE/1.PNG")
    binarizeAndErode(one, 2, 1, 150, True)
    nums.append(one)

    two = cv2.imread("ChipSE/2.PNG")
    two = cv2.cvtColor(two, cv2.COLOR_BGR2GRAY)
    two = cv2.threshold(two, 150, 255, cv2.THRESH_BINARY_INV)[1]
    nums.append(two)

    three = cv2.imread("PotSizeSE/3.PNG")
    three = binarizeAndErode(three, 2, 1, 150, True)
    nums.append(three)

    four = cv2.imread("ChipSE/4.PNG")
    four = binarizeAndErode(four, 1, 1, 150, True)
    y, x = four.shape[:2]
    four = four[0:y - 19, 0:x]
    nums.append(four)

    five = cv2.imread("PotSizeSE/5.PNG")
    five = binarizeAndErode(five, 1, 1, 137, True)
    nums.append(five)

    six = cv2.imread("PotSizeSE/6.PNG")
    six = binarizeAndErode(six, 2, 1, 150, True)
    nums.append(six)

    seven = cv2.imread("PotSizeSE/7.PNG")
    seven = binarizeAndErode(seven, 2, 1, 150, True)
    nums.append(seven)

    eight = cv2.imread("ChipSE/8.PNG")
    y, x = eight.shape[:2]
    eight = eight[0:y - 19, 0:x]
    eight = binarizeAndErode(eight, 1, 1, 150, True)
    nums.append(eight)

    nine = cv2.imread("ChipSE/9.PNG")
    nine = binarizeAndErode(nine, 2, 1, 150, True)
    nums.append(nine)

    return nums