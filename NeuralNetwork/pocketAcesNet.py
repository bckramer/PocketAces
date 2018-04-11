
import numpy as np
import time
import sys
if sys.version_info.major == 2:
#TODO adapt class to actual methods in rest of project
 class pocketAcesNet(object):
    def __init__(self):
        super(pocketAcesNet, self).__init__()
        self.action_space = ['c', 'f', 'r', 'b', 'a']
        self.n_actions = len(self.action_space)
        self.n_features = 5

    def reset(self):
        self.update()
        time.sleep(0.1)
        resetGame();
        # return observation
        return [curentChips(),opponentChips(),publicCards(),yourCards(),callSize()];


    def step(self, action):
        s = [curentChips(),opponentChips(),publicCards(),yourCards(),callSize()]; #Current State
        base_action = np.array([0, 0])
        if action == 0:   # call
            call()
        elif action == 1:   # fold
            fold()
        elif action == 2:   # raise
            raise(raiseBetAmount)
        elif action == 3:   # bet
            bet(raiseBetAmount)
        elif action == 4: #all in
            allIn()


        next_coords = self.canvas.coords(self.rect)

        # reward function
        reward = chipDifference()
        done = True

        s_ = [curentChips(),opponentChips(),publicCards(),yourCards(),callSize()]; # next State
        return s_, reward, done

    def render(self):
        # time.sleep(0.01)
        self.update()