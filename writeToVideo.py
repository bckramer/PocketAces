import numpy as np
import cv2
from PIL import ImageGrab
from ScreenRead import *
from Utils import *

# VERY IMPORTANT: Without it, the entire screen will not be captured
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1920,1080))
font = cv2.FONT_HERSHEY_SIMPLEX
# card1Value, card1Suit, card2Value, card2Suit, publicCardValue0, publicCardValue1, publicCardValue2, publicCardValue3, publicCardValue4, intSuits, potSize, playerPot
while(True):

    frame = np.array(ImageGrab.grab())

    values = getAllValues(0)
    # print(values[1])
    # print(values[3])
    card1Name, card1Suit = getReadableCard(int(values[0]), int(values[1]))
    card2Name, card2Suit = getReadableCard(int(values[2]), int(values[3]))
    cv2.putText(frame, "Player Cards", (275, 20), font, .7, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, card1Name + " of " + card1Suit, (275, 52), font, .7, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, card2Name + " of " + card2Suit, (275, 102), font, .7, (0, 255, 0), 2, cv2.LINE_AA)

    publicCards = []
    publicCards.extend((values[4], values[5], values[6], values[7], values[8]))
    cv2.putText(frame, "Public Cards", (275, 152), font, .7, (0, 255, 0), 2, cv2.LINE_AA)
    i = 0
    j = 0
    for card in publicCards:
        suits = str(values[9])
        if card != "0" and suits != "0":
            print(str(card))
            cardName, cardSuit = getReadableCard(int(card), int(suits[i]))
            cv2.putText(frame, cardName + " of " + cardSuit, (275, 202 + (i * 50)), font, .7, (0, 255, 0), 2, cv2.LINE_AA)
            i = i + 1
        j = j + 1

    cv2.putText(frame, "Player Pot: " + str(values[11]), (275, 500), font, .7, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "Public Pot: " + str(values[10]), (275, 550), font, .7, (0, 255, 0), 2, cv2.LINE_AA)
    # TODO Add Reward
    # small = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # cv2.imshow("frame", small)

    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


out.release()