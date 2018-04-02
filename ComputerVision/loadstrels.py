from Utils import *
import cv2

def loadPlayerStrels():
    strels = []

    two = cv2.imread('PlayerSE/2.PNG', cv2.IMREAD_GRAYSCALE)
    two = binarizeAndErode(two, 2, 1, 210, False)
    strels.append(two)

    three = cv2.imread('PlayerSE/3.PNG', cv2.IMREAD_GRAYSCALE)
    three = binarizeAndErode(three, 2, 1, 210, False)
    strels.append(three)

    four = cv2.imread('PlayerSE/4.PNG', cv2.IMREAD_GRAYSCALE)
    four = binarizeAndErode(four, 2, 1, 210, False)
    strels.append(four)

    five = cv2.imread('PlayerSE/5.PNG', cv2.IMREAD_GRAYSCALE)
    five = binarizeAndErode(five, 2, 1, 210, False)
    strels.append(five)

    six = cv2.imread('PlayerSE/6.PNG', cv2.IMREAD_GRAYSCALE)
    six = binarizeAndErode(six, 2, 1, 210, False)
    strels.append(six)

    seven = cv2.imread('PlayerSE/7.PNG', cv2.IMREAD_GRAYSCALE)
    seven = binarizeAndErode(seven, 2, 1, 210, False)
    strels.append(seven)

    eight = cv2.imread('PlayerSE/8.PNG', cv2.IMREAD_GRAYSCALE)
    eight = binarizeAndErode(eight, 2, 1, 210, False)
    strels.append(eight)

    nine = cv2.imread('PlayerSE/9.PNG', cv2.IMREAD_GRAYSCALE)
    nine = binarizeAndErode(nine, 2, 1, 210, False)
    strels.append(nine)

    ten = cv2.imread('PlayerSE/10.PNG', cv2.IMREAD_GRAYSCALE)
    ten = binarizeAndErode(ten, 2, 1, 210, False)
    strels.append(ten)

    jack = cv2.imread('PlayerSE/J.PNG', cv2.IMREAD_GRAYSCALE)
    jack = binarizeAndErode(jack, 2, 1, 210, False)
    strels.append(jack)

    queen = cv2.imread('PlayerSE/Q.PNG', cv2.IMREAD_GRAYSCALE)
    queen = binarizeAndErode(queen, 2, 1, 210, False)
    strels.append(queen)

    king = cv2.imread('PlayerSE/K.PNG', cv2.IMREAD_GRAYSCALE)
    king = binarizeAndErode(king, 2, 1, 210, False)
    strels.append(king)

    ace = cv2.imread('PlayerSE/A.PNG', cv2.IMREAD_GRAYSCALE)
    ace = binarizeAndErode(ace, 2, 2, 210, False)
    strels.append(ace)

    return strels

def loadSuitStrels():
    suits = []

    spade = cv2.imread("PlayerSE/Spade.PNG", cv2.IMREAD_GRAYSCALE)
    spade = binarizeAndErode(spade, 2, 1, 210, False)
    suits.append(spade)

    club = cv2.imread("PlayerSE/Club.PNG", cv2.IMREAD_GRAYSCALE)
    club = binarizeAndErode(club, 2, 1, 210, False)
    suits.append(club)

    heart = cv2.imread("PlayerSE/Heart.PNG", cv2.IMREAD_GRAYSCALE)
    heart = binarizeAndErode(heart, 2, 1, 210, False)
    suits.append(heart)

    diamond = cv2.imread("PlayerSE/Diamond.PNG", cv2.IMREAD_GRAYSCALE)
    diamond = binarizeAndErode(diamond, 2, 1, 210, False)
    suits.append(diamond)

    return suits

def loadPotSizeStrels():
    nums = []

    dollar = cv2.imread("PotSizeSE/$.PNG", cv2.IMREAD_GRAYSCALE)
    dollar = binarizeAndErode(dollar, 2, 1, 150, True)
    nums.append(dollar)

    zero = cv2.imread("PotSizeSE/0.PNG", cv2.IMREAD_GRAYSCALE)
    zero = binarizeAndErode(zero, 2, 1, 150, True)
    nums.append(zero)

    one = cv2.imread("PotSizeSE/1.PNG", cv2.IMREAD_GRAYSCALE)
    one = binarizeAndErode(one, 1, 1, 150, True)
    nums.append(one)

    two = cv2.imread("PotSizeSE/2.PNG", cv2.IMREAD_GRAYSCALE)
    two = binarizeAndErode(two, 2, 1, 150, True)
    nums.append(two)

    three = cv2.imread("PotSizeSE/3.PNG", cv2.IMREAD_GRAYSCALE)
    three = binarizeAndErode(three, 1, 1, 150, True)
    nums.append(three)

    four = cv2.imread("PotSizeSE/4.PNG", cv2.IMREAD_GRAYSCALE)
    four = binarizeAndErode(four, 1, 1, 150, True)
    nums.append(four)

    five = cv2.imread("PotSizeSE/5.PNG", cv2.IMREAD_GRAYSCALE)
    five = binarizeAndErode(five, 2, 1, 137, True)
    nums.append(five)

    six = cv2.imread("PotSizeSE/6.PNG", cv2.IMREAD_GRAYSCALE)
    six = binarizeAndErode(six, 2, 1, 150, True)
    nums.append(six)

    seven = cv2.imread("PotSizeSE/7.PNG", cv2.IMREAD_GRAYSCALE)
    seven = binarizeAndErode(seven, 1, 1, 150, True)
    nums.append(seven)

    eight = cv2.imread("PotSizeSE/8.PNG", cv2.IMREAD_GRAYSCALE)
    eight = binarizeAndErode(eight, 1, 1, 150, True)
    nums.append(eight)

    nine = cv2.imread("PotSizeSE/9.PNG", cv2.IMREAD_GRAYSCALE)
    nine = binarizeAndErode(nine, 1, 1, 150, True)
    nums.append(nine)

    return nums

def loadPublicStrels():
    strels = []

    two = cv2.imread('PublicCardsSE/2.PNG', cv2.IMREAD_GRAYSCALE)
    two = binarizeAndErode(two, 1, 1, 210, False)
    strels.append(two)

    three = cv2.imread('PublicCardsSE/3.PNG', cv2.IMREAD_GRAYSCALE)
    three = binarizeAndErode(three, 2, 1, 210, False)
    strels.append(three)

    four = cv2.imread('PublicCardsSE/4.PNG', cv2.IMREAD_GRAYSCALE)
    four = binarizeAndErode(four, 1, 1, 210, False)
    strels.append(four)

    five = cv2.imread('PublicCardsSE/5.PNG', cv2.IMREAD_GRAYSCALE)
    five = binarizeAndErode(five, 2, 1, 210, False)
    strels.append(five)

    six = cv2.imread('PublicCardsSE/6.PNG', cv2.IMREAD_GRAYSCALE)
    six = binarizeAndErode(six, 3, 1, 210, False)
    strels.append(six)

    seven = cv2.imread('PublicCardsSE/7.PNG', cv2.IMREAD_GRAYSCALE)
    seven = binarizeAndErode(seven, 2, 1, 210, False)
    strels.append(seven)

    eight = cv2.imread('PublicCardsSE/8.PNG', cv2.IMREAD_GRAYSCALE)
    eight = binarizeAndErode(eight, 3, 1, 210, False)
    strels.append(eight)

    nine = cv2.imread('PublicCardsSE/9.PNG', cv2.IMREAD_GRAYSCALE)
    nine = binarizeAndErode(nine, 5, 1, 210, False)
    strels.append(nine)

    ten = cv2.imread('PublicCardsSE/10.PNG', cv2.IMREAD_GRAYSCALE)
    ten = binarizeAndErode(ten, 2, 1, 210, False)
    strels.append(ten)

    jack = cv2.imread('PublicCardsSE/J.PNG', cv2.IMREAD_GRAYSCALE)
    jack = binarizeAndErode(jack, 3, 1, 210, False)
    strels.append(jack)

    queen = cv2.imread('PublicCardsSE/Q.PNG', cv2.IMREAD_GRAYSCALE)
    queen = binarizeAndErode(queen, 2, 1, 210, False)
    strels.append(queen)

    king = cv2.imread('PublicCardsSE/K.PNG', cv2.IMREAD_GRAYSCALE)
    king = binarizeAndErode(king, 2, 1, 210, False)
    strels.append(king)

    ace = cv2.imread('PublicCardsSE/A.PNG', cv2.IMREAD_GRAYSCALE)
    ace = binarizeAndErode(ace, 2, 1, 210, False)
    strels.append(ace)

    return strels

def loadChipCountStrels():
    nums = []

    dollar = cv2.imread("ChipSE/$.PNG", cv2.IMREAD_GRAYSCALE)
    dollar = binarizeAndErode(dollar, 1, 1, 150, True)
    y, x = dollar.shape[:2]
    dollar = dollar[0:y, 60:x]
    nums.append(dollar)

    zero = cv2.imread("ChipSE/0.PNG", cv2.IMREAD_GRAYSCALE)
    zero = binarizeAndErode(zero, 1, 1, 150, True)
    nums.append(zero)

    one = cv2.imread("ChipSE/1.PNG", cv2.IMREAD_GRAYSCALE)
    binarizeAndErode(one, 3, 1, 150, True)
    y, x = one.shape[:2]
    one = one[0:y, 0:x - 24]
    cv2.imshow("one", one)
    nums.append(one)

    two = cv2.imread("ChipSE/2.PNG", cv2.IMREAD_GRAYSCALE)
    two = cv2.threshold(two, 150, 255, cv2.THRESH_BINARY_INV)[1]
    nums.append(two)

    three = cv2.imread("PotSizeSE/3.PNG", cv2.IMREAD_GRAYSCALE)
    three = binarizeAndErode(three, 2, 1, 150, True)
    nums.append(three)

    four = cv2.imread("ChipSE/4.PNG", cv2.IMREAD_GRAYSCALE)
    four = binarizeAndErode(four, 1, 1, 150, True)
    y, x = four.shape[:2]
    four = four[0:y - 19, 0:x]
    nums.append(four)

    five = cv2.imread("ChipSE/5.PNG", cv2.IMREAD_GRAYSCALE)
    five = binarizeAndErode(five, 0, 1, 137, True)
    y, x = five.shape[:2]
    five = five[0:y - 4, 0:x - 10]
    nums.append(five)

    six = cv2.imread("ChipSE/6.PNG", cv2.IMREAD_GRAYSCALE)
    six = binarizeAndErode(six, 1, 1, 150, True)
    y, x = six.shape[:2]
    six = six[0:y - 4, 0:x - 10]
    nums.append(six)

    seven = cv2.imread("PotSizeSE/7.PNG", cv2.IMREAD_GRAYSCALE)
    seven = binarizeAndErode(seven, 2, 1, 150, True)
    nums.append(seven)

    eight = cv2.imread("ChipSE/8.PNG", cv2.IMREAD_GRAYSCALE)
    y, x = eight.shape[:2]
    eight = eight[0:y - 19, 0:x]
    eight = binarizeAndErode(eight, 1, 1, 150, True)
    nums.append(eight)

    nine = cv2.imread("ChipSE/9.PNG", cv2.IMREAD_GRAYSCALE)
    nine = binarizeAndErode(nine, 1, 1, 150, True)
    nums.append(nine)

    return nums