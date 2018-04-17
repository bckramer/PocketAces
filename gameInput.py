from pynput.keyboard import Key, Controller
from ScreenRead import getAllValues
import time

keyboard = Controller()
time.sleep(1)

def call():
    keyboard.press('c')
    keyboard.release('c')

def bet(betAmount):
    for i in range(0, betAmount):
        time.sleep(.02)
        keyboard.press(Key.up)
    keyboard.press('b')
    keyboard.release('b')
    keyboard.press('r')
    keyboard.release('r')

def allIn():
    keyboard.press('a')

def raise1(betAmount):
    for i in range(0, betAmount):
        time.sleep(.02)
        keyboard.press(Key.up)
    keyboard.press('r')
    keyboard.release('r')
    keyboard.press('b')
    keyboard.release('b')

def fold():
    keyboard.press('f')
    keyboard.release('f')

def deal():
    keyboard.press('d')
    keyboard.release('d')

def continue1():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def keyInputRaise(betAmount):
    betAmount = betAmount -1
    betAmountString = str(betAmount)
    for i in range(0, len(betAmountString)):
        keyboard.press(betAmountString[i])
        keyboard.release(betAmountString[i])
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press('b')
    keyboard.release('b')
    keyboard.press('r')
    keyboard.release('r')


