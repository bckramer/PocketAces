from pynput.keyboard import Key, Controller
from ScreenRead import getAllValues
import time

keyboard = Controller()
time.sleep(1)

def call():
    keyboard.press('c')

def bet(betAmount):
    for i in range(0, betAmount):
        time.sleep(.02)
        keyboard.press(Key.up)
    keyboard.press('b')
    keyboard.press('r')

def allIn():
    keyboard.press('a')

def raise1(betAmount):
    for i in range(0, betAmount):
        time.sleep(.02)
        keyboard.press(Key.up)
    keyboard.press('r')
    keyboard.press('b')

def fold():
    keyboard.press('f')

def deal():
    keyboard.press('d')

def continue1():
    keyboard.press('c')

def keyInputRaise(betAmount):
    betAmount = betAmount -1
    betAmountString = str(betAmount)
    print("Bet Amount "  + betAmount)
    print(betAmountString)
    for i in range(0, len(betAmountString)):
        keyboard.press(betAmountString[i])
        print(str(betAmountString[i]))
    keyboard.press(Key.up)
    keyboard.press('b')
    keyboard.press('r')


