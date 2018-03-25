# Below is a simple way to grab the entire screen in 1920x1080,
# but it should work in other resolutions.
import numpy as np
from Utils import loadPlayeSE
from PIL import ImageGrab
import cv2
# VERY IMPORTANT: Without it, the entire screen will not be captured
from ctypes import windll

user32 = windll.user32
user32.SetProcessDPIAware()

#Finds the cards in the users hand
def findCards(cardsImage):
    kernel = np.ones((1, 1), np.uint8)
    strels = loadPlayeSE()
    card1Image = cv2.bitwise_not(cardsImage[8:50, 12:50])
    card1Image = cv2.erode(card1Image, kernel, iterations=1)
    card2Image = cv2.bitwise_not(cardsImage[20:58, 48:80])
    card2Image = cv2.erode(card2Image, kernel, iterations=1)
    cardImages = []
    cardImages.append(card1Image)
    cardImages.append(card2Image)
    cards = []
    card1 = 0
    card2 = 0
    cards.append(card1)
    cards.append(card2)
    i = 0
    for card in cardImages:
        j = 2
        for strel in strels:
            erosion = cv2.erode(card, strel, iterations = 1)
            im, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE,
                                                        cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) == 1:
                cv2.imshow("card", card)
                cv2.imshow("im", im)
                cv2.imshow("strel", strel)
                cards[i] = j
            j = j + 1
        i = i + 1
    curCards = ''
    for card in cards:
        curCards = curCards + " " + str(card)
    print curCards

while True:
    screen_grab = ImageGrab.grab()
    # Converted to an array OpenCV can use.
    cv_image = np.array(screen_grab, dtype='uint8')
    # cv2.imshow('window', printscreen_numpy)
    cv_image_grey = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    thresh, cv_image_bw = cv2.threshold(cv_image_grey, 200, 255, cv2.THRESH_BINARY)
    cards = cv_image_bw[620:795, 1000:1200]
    resize = cv2.resize(cv_image_bw, (1280, 720))
    findCards(cards)
    cv2.imshow("Cards", cards)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

