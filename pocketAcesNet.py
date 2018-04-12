import numpy as np
import time
import sys
from gameInput import *
from ScreenRead import *
lastChips = 100
newChips = 0


# if sys.version_info.major == 2:#TODO adapt class to actual methods in rest of project

raiseBetAmount = 10
class PocketAces(object):
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
        time.sleep(2)
        base_action = np.array([0, 0])
        if action == 0:  # call
            call()
            print("call")
        elif action == 1:  # fold
            fold()
            print("fold")
        elif action == 2:  # raise
            raise1(raiseBetAmount)
            print("raise")
        elif action == 3:  # bet
            bet(raiseBetAmount)
            print("bet")
        elif action == 4:  # all in
            allIn()
            print("allin")

        # next_coords = self.canvas.coords(self.rect)

        # reward function
        dealButton, foldButton, checkCallButtons, raiseButton, allInButton = buttonsAvailable()
        if dealButton == True:
            newChips = getAllValues()[11]
            lastChips = newChips
            chipDifference = lastChips - newChips
            reward = chipDifference
        else:
            reward = 0



        done = True

        s_ = getAllValues()  # next State

        return s_, reward, done

    def render(self):
        # time.sleep(0.01)
        # self.update()
        return
