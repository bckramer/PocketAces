from pocketAcesNet import PocketAces
from RL_brain import DeepQNetwork
from RL_brain import *

import cv2
import time


def run_pocket_aces():
        step = 0
        time.sleep(2) #allows user to click off into DD Poker 3

        RL.load("save/build3")
        for episode in range(100):

            # initial observation
            observation = env.reset()
            while True:

            # fresh env
               # gameStart(); commented for testing

                # RL choose action based on observation
                action = RL.choose_action(observation)


                # RL take action and get next observation and reward
                observation_, reward, done = env.step(action)

                RL.store_transition(observation, action, reward, observation_)

                if (step > 200) and (step % 5 == 0):
                    RL.learn()

                # swap observation
                observation = observation_

                #saving, MAKE SURE SAVE DIRECTORY IS DELETED
                # if episode == 3000:
                #     RL.save(observation, action, reward, observation_, "save/save1")
                #     RL.build("save/build1")
                #
                # if episode == 6000:
                #      RL.save(observation, action, reward, observation_,"save/save2")
                #      RL.build("save/build2")
                #
                # if episode == 9900:
                #     RL.save(observation, action, reward, observation_, "save/save3")
                #     RL.build("save/build3")

                # break while loop when end of this episode
                if done:
                    break
                step += 1

                if cv2.waitKey(30) & 0xFF == ord('q'):
                    break

        # end of game
        print('game over')
        #stopGame() commented for testing


if __name__ == "__main__":
    # maze game
    env = PocketAces()
    RL = DeepQNetwork(env.n_actions, env.n_features,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=10000,
                      memory_size=100000,
                      # output_graph=True
                      )
    #env.after(100, run_pocket_aces)
    run_pocket_aces()
    RL.plot_cost()
