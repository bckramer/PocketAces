
import numpy as np
import time
import sys
from testFunctions import *
#if sys.version_info.major == 2:#TODO adapt class to actual methods in rest of project
class PocketAces(object):
    def __init__(self):
        super(PocketAces, self).__init__()
        self.action_space = ['c', 'f', 'r', 'b', 'a']
        self.n_actions = len(self.action_space)
        self.n_features = 5

    def reset(self):
        #self.update()
        time.sleep(0.1)
        #resetGame(); commented for testing
        # return observation
        return np.array([currentChips(), opponentChips(), publicCards(), yourCards(), callSize()])


    def step(self, action):
        s = np.array([currentChips(), opponentChips(), publicCards(), yourCards(), callSize()]) #Current State
        base_action = np.array([0, 0])
        if action == 0:   # call
            call(10)
            print("call")
        elif action == 1:   # fold
            fold()
            print("fold")
        elif action == 2:   # raise
            raise1(raiseBetAmount)
            print("raise")
        elif action == 3:   # bet
            bet(raiseBetAmount)
            print("bet")
        elif action == 4: #all in
            allIn()
            print("allin")


        #next_coords = self.canvas.coords(self.rect)

        # reward function
        reward = chipDifference()
        done = True

        s_ = np.array([currentChips(), opponentChips(), publicCards(), yourCards(), callSize()]) # next State
        return s_, reward, done

    def render(self):
        #time.sleep(0.01)
        #self.update()
        return
