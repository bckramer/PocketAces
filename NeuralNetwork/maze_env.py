
import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['c', 'f', 'r', 'b', 'a']
        self.n_actions = len(self.action_space)
        self.n_features = 2


    def step(self, action):
        s = self.canvas.coords(self.rect)
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


        next_coords = self.canvas.coords(self.rect)  # next state

        # reward function
        reward = chipDifference
        done = True

        s_ = chipDifference#(np.array(next_coords[:2]) - np.array(self.canvas.coords(self.oval)[:2]))/(MAZE_H*UNIT)
        return s_, reward, done

    def render(self):
        # time.sleep(0.01)
        self.update()