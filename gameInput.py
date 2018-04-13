from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(1)

def call():
    keyboard.press('c')

def bet(betAmount):
    for i in range(0, betAmount):
        keyboard.press(Key.up)
    keyboard.press('b')

def allIn():
    keyboard.press('a')

def raise1(betAmount):
    for i in range(0, betAmount):
        time.sleep(.05)
        keyboard.press(Key.up)
    keyboard.press('r')

def fold():
    keyboard.press('f')

def deal():
    keyboard.press('d')

def continue1():
    keyboard.press('c')
