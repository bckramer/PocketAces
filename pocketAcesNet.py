import numpy as np
import time
import sys
from gameInput import *
from ScreenRead import *
# if sys.version_info.major == 2:#TODO adapt class to actual methods in rest of project

raiseBetAmount = 10
class PocketAces(object):
    lastChips = 100
    newChips = 0
    def __init__(self):
        super(PocketAces, self).__init__()
        self.action_space = ['c', 'f', 'r', 'b', 'a']
        self.n_actions = len(self.action_space)
        self.n_features = 12

    def reset(self):
        # self.update()
        time.sleep(0.1)
        # resetGame(); commented for testing
        # return observation
        return getAllValues()

    def step(self, action):
        s = getAllValues() #current state
        base_action = np.array([0, 0])
        dealButton, foldButton, checkButton, raiseButton, allInButton, continueButton = buttonsAvailable()
        if(continueButton == True):
            continue1()

        while not (dealButton and foldButton and checkButton and raiseButton and allInButton):
            time.sleep(.05)
            dealButton, foldButton, checkButton, raiseButton, allInButton, continueButton = buttonsAvailable()

        if action == 0:  # call
            call()
            print("call")
        elif action == 1:  # fold
            fold()
            print("fold")
        elif action == 2 and raiseButton:  # raise
            raise1(raiseBetAmount)
            print("raise")
        elif action == 3 and raiseButton:  # bet
            bet(raiseBetAmount)
            print("bet")
        elif action == 4:  # all in
            allIn()
            print("allin")
        else:
            fold()
            print("fold")

        # reward function
        if dealButton == True:
            newChips = getAllValues()[11]
            lastChips = newChips
            chipDifference = int(lastChips) - int(newChips)
            reward = chipDifference
            deal()
        else:
            reward = 0
        done = True

        s_ = getAllValues()  # next State

        return s_, reward, done

    def render(self):
        # time.sleep(0.01)
        # self.update()
        return
