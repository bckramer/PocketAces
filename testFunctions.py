import random
import numpy as np
import tensorflow as tf

raiseBetAmount = 10  # FOR TESTING


def currentChips():
    return random.randrange(100)


def opponentChips():
    return random.randrange(100)


def publicCard0():
    return random.randrange(10)


def publicCard1():
    return random.randrange(10)


def publicCard2():
    return random.randrange(10)


def publicCard3():
    return random.randrange(10)


def publicCard4():
    return random.randrange(10)


def publicSuit0():
    return random.randrange(10)


def publicSuit1():
    return random.randrange(10)


def publicSuit2():
    return random.randrange(10)


def publicSuit3():
    return random.randrange(10)


def publicSuit4():
    return random.randrange(10)


def yourCard1():
    return random.randrange(10)


def yourCard2():
    return random.randrange(10)


def yourSuit1():
    return random.randrange(10)


def yourSuit2():
    return random.randrange(10)

def callSize():
    return random.randrange(50)


def call(raiseBetAmount):
    return


def raise1(raiseBetAmount):
    return


def bet(raiseBetAmount):
    return


def fold():
    return


def allIn():
    return


def chipDifference():
    return 10
