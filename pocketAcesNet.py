import numpy as np
import time
import sys
from gameInput import *
from mouseCommands import *
from ScreenRead import *
# if sys.version_info.major == 2:#TODO adapt class to actual methods in rest of project
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

raiseBetAmount = 10
class PocketAces(object):
    newChips = 0
    def __init__(self):
        super(PocketAces, self).__init__()
        self.action_space = ['c', 'f', 'r1','r2','r3', 'a']
        self.n_actions = len(self.action_space)
        self.n_features = 13
        self.lastChips = 1000
        self.currentPot = 0
        self.prevPot = 0
        self.newTournament = True

    def reset(self):
        # self.update()
        time.sleep(0.1)
        # resetGame(); commented for testing
        # return observation
        return getAllValues(self.prevPot)

    def step(self, action):
        s = getAllValues(self.prevPot) #current state
        base_action = np.array([0, 0])
        dealButton, foldButton, checkButton, raiseButton, allInButton, continueButton, playAgainButton = buttonsAvailable()
        if self.newTournament == True:
            self.lastChips = s[11]
            self.newTournament = False

        timeWaited = 0
        while not dealButton and not foldButton and not checkButton and not raiseButton and not allInButton and not continueButton:
            time.sleep(.05)
            dealButton, foldButton, checkButton, raiseButton, allInButton, continueButton, playAgainButton = buttonsAvailable()
            timeWaited = timeWaited + 0.05
            if timeWaited > 2:
                continue1()
        if action == 0:  # call
            call()
            print("call")
        elif action == 1 and foldButton:  # fold
            fold()
            print("fold")
        elif action == 2 and raiseButton:  # raise
            potSize = int(s[11])
            keyInputRaise(int(potSize/5))
            print("raise")
        elif action == 3 and raiseButton:  # bet
            potSize = int(s[11])
            keyInputRaise(int(potSize/4))
            print("bet")
        elif action == 4 and raiseButton:  # bet
            potSize = int(s[11])
            keyInputRaise(int(potSize/10))
            print("bet")
        elif action == 5:  # all in
            allIn()
            print("allin")
        else:
            call()
            print("call")
        time.sleep(1)
        # reward function
        if playAgainButton == True:
            playAgain()
            self.newTournament = True
            print("play again")
        if dealButton == True:
            newValues = getAllValues(self.prevPot)
            newChips = str(newValues[11])
            chipDifference = int(newChips) - int(self.lastChips)
            self.lastChips = int(newChips)
            self.currentPot = 0
            self.prevPot = 0
            reward = chipDifference
            deal()
        else:
            reward = 0
        done = True
        self.prevPot = s[10]
        s_ =  getAllValues(self.prevPot) # next State

        return s_, reward, done

    def render(self):
        # time.sleep(0.01)
        # self.update()
        return
