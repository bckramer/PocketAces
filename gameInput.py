from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(1)

def call():
    keyboard.press('c')

def bet(betAmount):
    keyboard.press('b')
    for i in range(0, betAmount):
        keyboard.press('up')

def allIn():
    keyboard.press('a')

def raise1(betAmount):
    keyboard.press('r')
    for i in range(0, betAmount):
        keyboard.press(Key.up)

def fold():
    keyboard.press('f')

def deal():
    keyboard.press('d')

def continoue():
    keyboard.press('c')
