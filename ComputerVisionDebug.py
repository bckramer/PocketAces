# Run this script to verify information about the game
# is being read correctly
import numpy as np
from Utils import *
from findcontours import *
from loadstrels import *
from PIL import ImageGrab
from findvalues import *
from ScreenRead import *
import cv2
import time
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

newPotSizeStrels = loadPotSizeStrels()
callSize = 0
prevPotSize = 0
while True:
    values = getAllValues(0)
    buttons = buttonsAvailable()
    print("Pot size: " + str(values[10]) + " Player Pot: " + str(values[11]))
    suits = str(values[9])
    print("")
    print("Public Cards")
    printCard(values[4], int(suits[0]))
    if suits != "0":
        printCard(values[5], int(suits[1]))
    if suits != "0":
        printCard(values[6], int(suits[2]))
    if suits != "0":
        printCard(values[7], int(suits[3]))
    if suits != "0":
        printCard(values[8], int(suits[4]))
    print("")
    print("Player Cards")
    printCard(values[0], values[1])
    printCard(values[2], values[3])
    print("-------------------")
    time.sleep(2)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

