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
        # The players most recent amount of chips
        self.lastChips = 0
        # The pot size of the last game. Used for calculating opponents raise size
        self.prevPot = 0
        # When a new tournament begins, the player pot
        # is reset. Using this value allows us
        # to reset it for the net as well.
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
        done = False
        dealButton, foldButton, checkButton, raiseButton, allInButton, continueButton, playAgainButton = buttonsAvailable()
        if self.newTournament == True:
            tempPlayerPotSize = s[11]
            self.lastChips = tempPlayerPotSize
            self.newTournament = False

        timeWaited = 0
        while not dealButton and not foldButton and not checkButton and not raiseButton and not allInButton:
            time.sleep(.05)
            dealButton, foldButton, checkButton, raiseButton, allInButton, continueButton, playAgainButton = buttonsAvailable()
            timeWaited = timeWaited + 0.05
            if timeWaited > .5:
                continue1()
        if action == 0:  # call
            call()
            # print("call")
        elif action == 1 and foldButton:  # fold
            fold()
            # print("fold")
        elif action == 2 and raiseButton:  # raise
            playerPot = int(s[11])
            keyInputRaise(int(playerPot/20))
            # print("raise")
        elif action == 3 and raiseButton:  # bet
            playerPot = int(s[11])
            keyInputRaise(int(playerPot/4))
            # print("bet")
        elif action == 4 and raiseButton:  # bet
            playerPot = int(s[11])
            keyInputRaise(int(playerPot/10))
            # print("bet")
        elif action == 5:  # all in
            allIn()
            # print("allin")
        else:
            call()
            # print("call")
        # reward function
        if playAgainButton == True:
            playAgain()
            self.newTournament = True
            print("play again")
            f = open('csv/session3/trainingSession3_loaded_PlayAgainCounter-positiveRewards.csv', 'a')
            f.write("PLAY_AGAIN")
            f.write('\n')
            f.close()
        if dealButton == True:
            newValues = getAllValues(self.prevPot)
            if newValues[11] != -1:
                newChips = str(newValues[11])
                chipDifference = int(newChips) - int(self.lastChips)
                self.lastChips = int(newChips)
                self.prevPot = 0
                reward = chipDifference
                temp = getAllValues(self.prevPot);
                f = open('csv/session3/trainingSession3_PlayerPot-positiveRewards.csv', 'a')
                if reward >= 0:
                    f.write(str(temp[11]) + "," + "WIN");
                else:
                    f.write(str(temp[11]) + "," + "LOSS");
                f.write('\n')
                f.close()
                if reward > 0:
                    done = True
            else:
                reward = 0;
            deal()
        else:
            reward = 0
        prevPot = s[10]
        self.prevPot = prevPot
        s_ =  getAllValues(self.prevPot) # next State

        return s_, reward, done

    def render(self):
        # time.sleep(0.01)
        # self.update()
        return
