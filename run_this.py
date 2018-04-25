from pocketAcesNet import PocketAces
from RL_brain import DeepQNetwork
from RL_brain import *
import random

import cv2
import time


# Built following the tutorial found at
# https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/5_Deep_Q_Network

def run_pocket_aces():
        step = 0
        time.sleep(2) #allows user to click off into DD Poker 3
        totalReward = 0
        for episode in range(50000):

            # saving, MAKE SURE SAVE DIRECTORY IS DELETED
            if episode == 1000:
                RL.save(observation, action, reward, observation_, "save/save0")

            if episode == 3000:
                RL.save(observation, action, reward, observation_, "save/save1")

            if episode == 6000:
                RL.save(observation, action, reward, observation_, "save/save2")

            if episode == 10000:
                RL.save(observation, action, reward, observation_, "save/save3")

            if episode == 12000:
                RL.save(observation, action, reward, observation_, "save/save4")

            if episode == 15000:
                RL.save(observation, action, reward, observation_, "save/save5")

            if episode == 20000:
                RL.save(observation, action, reward, observation_, "save/save6")

            if episode == 25000:
                RL.save(observation, action, reward, observation_, "save/save7")

            if episode == 30000:
                RL.save(observation, action, reward, observation_, "save/save8")

            if episode == 35000:
                RL.save(observation, action, reward, observation_, "save/save9")

            if episode == 40000:
                RL.save(observation, action, reward, observation_, "save/save10")

            if episode == 45000:
                RL.save(observation, action, reward, observation_, "save/save11")

            if episode == 49000:
                RL.save(observation, action, reward, observation_, "save/save12")

            if episode == 50000:
                RL.save(observation, action, reward, observation_, "save/save14")


            # initial observation
            observation = env.reset()
            reward = 0
            while True:

                # gameStart(); commented for testing
                # RL choose action based on observation
                action = RL.choose_action(observation)

                # RL take action and get next observation and reward
                observation_, reward, done = env.step(action)

                plotData = reward
                totalReward = totalReward + plotData
                f = open('csv/session3/trainingSession3_loaded_TotalReward-positiveRewards.csv', 'a')
                f.write(str(totalReward))
                f.write('\n')
                f.close()

                f = open('csv/session3/trainingSession3_loaded_AllInformation-positiveRewards.csv', 'a')
                for value in observation_:
                    f.write(str(value) + ",")
                f.write('\n')
                f.close()

                RL.store_transition(observation, action, reward, observation_)

                if (step > 200) and (step % 10 == 0):
                    RL.learn()

                # swap observation
                observation = observation_

                # break while loop when end of this episode
                if done:
                    break
                step = step + 1

                if cv2.waitKey(0) & 0xFF == ord('q'):
                    break

        # end of game
        print('game over')
        #stopGame() commented for testing


if __name__ == "__main__":
    env = PocketAces()
    RL = DeepQNetwork(env.n_actions, env.n_features,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.8,
                      replace_target_iter=500,
                      memory_size=45000,
                      output_graph=True
                      )
    # env.after(100, run_pocket_aces)
    run_pocket_aces()
    RL.plot_cost()
