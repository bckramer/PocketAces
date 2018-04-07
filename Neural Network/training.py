
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import random
import cntk as C


isFast = True
TOTAL_EPISODES = 2000 if isFast else 3000

isFast = True

#env = gym.make('CartPole-v0')

#STATE_COUNT  = env.observation_space.shape[0] STATE_COUNT = 4 (corresponding to (x,x˙,θ,θ˙)),
#ACTION_COUNT = env.action_space.n   ACTION_COUNT = 2 (corresponding to LEFT or RIGHT)
#
#
# STATE_COUNT, ACTION_COUNT

input_dim = 5
num_output_classes = 5
num_hidden_layers = 3
hidden_layers_dim = 6

STATE_COUNT = input_dim
ACTION_COUNT = num_output_classes

# Targetted reward
REWARD_TARGET = 200 if isFast else 2000 #total chips over training time
# Averaged over these these many episodes
BATCH_SIZE_BASELINE = 20 if isFast else 50

#H = 64 # hidden layer size


MEMORY_CAPACITY = 100000
BATCH_SIZE = 64

GAMMA = 0.99 # discount factor

MAX_EPSILON = 1
MIN_EPSILON = 0.01 # stay a bit curious even when getting old
LAMBDA = 0.0001    # speed of decay



if 'TEST_DEVICE' in os.environ:
    if os.environ['TEST_DEVICE'] == 'cpu':
        C.device.try_set_default_device(C.device.cpu())
    else:
        C.device.try_set_default_device(C.device.gpu(0))


class Brain:
    def __init__(self):
        self.params = {}
        self.model, self.trainer, self.loss = self._create()
        # self.model.load_weights("cartpole-basic.h5")

    def _create(self):
        #observation = C.sequence.input_variable(STATE_COUNT, np.float32, name="s")
        #q_target = C.sequence.input_variable(ACTION_COUNT, np.float32, name="q")

        observation = C.sequence.input_variable(input_dim, np.float32, name="s")
        q_target = C.sequence.input_variable(num_output_classes, np.float32, name="q") #total possible moves it can do from current state

        # Following a style similar to Keras
        l1 = C.layers.Dense(hidden_layers_dim, activation=C.relu)
        l2 = C.layers.Dense(ACTION_COUNT)
        unbound_model = C.layers.Sequential([l1, l2])
        model = unbound_model(observation)

        self.params = dict(W1=l1.W, b1=l1.b, W2=l2.W, b2=l2.b)

        # loss='mse'
        loss = C.reduce_mean(C.square(model - q_target), axis=0)
        meas = C.reduce_mean(C.square(model - q_target), axis=0)

        # optimizer
        lr = 0.00025
        lr_schedule = C.learning_parameter_schedule(lr)
        learner = C.sgd(model.parameters, lr_schedule, gradient_clipping_threshold_per_sample=10)
        trainer = C.Trainer(model, (loss, meas), learner)

        # CNTK: return trainer and loss as well
        return model, trainer, loss

    def train(self, x, y, epoch=1, verbose=0):
        #self.model.fit(x, y, batch_size=64, nb_epoch=epoch, verbose=verbose)
        arguments = dict(zip(self.loss.arguments, [x,y]))
        updated, results =self.trainer.train_minibatch(arguments, outputs=[self.loss.output])

    def predict(self, s):
        return self.model.eval([s])

class Memory:   # stored as ( s, a, r, s_ )
    samples = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add(self, sample):
        self.samples.append(sample)

        if len(self.samples) > self.capacity:
            self.samples.pop(0)

    def sample(self, n):
        n = min(n, len(self.samples))
        return random.sample(self.samples, n)



class Agent:
    steps = 0
    epsilon = MAX_EPSILON

    def __init__(self):
        self.brain = Brain()
        self.memory = Memory(MEMORY_CAPACITY)

    def act(self, s):
        if random.random() < self.epsilon:
            return random.randint(0, ACTION_COUNT-1)
        else:
            return np.argmax(self.brain.predict(s))

    def observe(self, sample):  # in (s, a, r, s_) format
        self.memory.add(sample)

        # slowly decrease Epsilon based on our eperience
        self.steps += 1
        self.epsilon = MIN_EPSILON + (MAX_EPSILON - MIN_EPSILON) * np.math.exp(-LAMBDA * self.steps)

    def replay(self):
        batch = self.memory.sample(BATCH_SIZE)
        batchLen = len(batch)

        no_state = np.zeros(STATE_COUNT)


        # CNTK: explicitly setting to float32
        states = np.array([ o[0] for o in batch ], dtype=np.float32)
        states_ = np.array([(no_state if o[3] is None else o[3]) for o in batch ], dtype=np.float32)

        p = agent.brain.predict(states)
        p_ = agent.brain.predict(states_)

        # CNTK: explicitly setting to float32
        x = np.zeros((batchLen, STATE_COUNT)).astype(np.float32)
        y = np.zeros((batchLen, ACTION_COUNT)).astype(np.float32)

        for i in range(batchLen):
            s, a, r, s_ = batch[i]

            # CNTK: [0] because of sequence dimension
            t = p[0][i]
            if s_ is None:
                t[a] = r
            else:
                t[a] = r + GAMMA * np.amax(p_[0][i])

            x[i] = s
            y[i] = t

        self.brain.train(x, y)


def plot_weights(weights, figsize=(7,5)):
    '''Heat map of weights to see which neurons play which role'''
    sns.set(style="white")
    f, ax = plt.subplots(len(weights), figsize=figsize)
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    for i, data in enumerate(weights):
        axi = ax if len(weights)==1 else ax[i]
        if isinstance(data, tuple):
            w, title = data
            axi.set_title(title)
        else:
            w = data

        sns.heatmap(w.asarray(), cmap=cmap, square=True, center=True, #annot=True,
                    linewidths=.5, cbar_kws={"shrink": .25}, ax=axi)

def epsilon(steps):
    return MIN_EPSILON + (MAX_EPSILON - MIN_EPSILON) * np.exp(-LAMBDA * steps)
plt.plot(range(10000), [epsilon(x) for x in range(10000)], 'r')
plt.xlabel('step');plt.ylabel('$\epsilon$')

def run(agent):
    #s = initGame() # TODO need to set initial game state for game
    R = 0

    while True:


        # CNTK: explicitly setting to float32
        a = agent.act(s.astype(np.float32))

        s_, r, done, info = env.step(a)

        if done: # terminal state
            s_ = None

        agent.observe((s, a, r, s_))
        agent.replay()

        s = s_
        R += r

        if done:
            return R

agent = Agent()

episode_number = 0
reward_sum = 0
while episode_number < TOTAL_EPISODES:
    reward_sum += run(agent)
    episode_number += 1
    if episode_number % BATCH_SIZE_BASELINE == 0:
        print('Episode: %d, Average reward for episode %f.' % (episode_number,
                                                               reward_sum / BATCH_SIZE_BASELINE))
        if episode_number%200==0:
            plot_weights([(agent.brain.params['W1'], 'Episode %i $W_1$'%episode_number)], figsize=(14,5))
        if reward_sum / BATCH_SIZE_BASELINE > REWARD_TARGET:
            print('Task solved in %d episodes' % episode_number)
            plot_weights([(agent.brain.params['W1'], 'Episode %i $W_1$'%episode_number)], figsize=(14,5))
            break
        reward_sum = 0

agent.brain.model.save('dqn.mod')

num_episodes = 10  # number of episodes to run

modelPath = 'dqn.mod'
root = C.load_model(modelPath)

for i_episode in range(num_episodes):
    print(i_episode)
    #observation = env.reset()  # TODO reset environment for new episode
    done = False
    while not done:
        action = np.argmax(root.eval([observation.astype(np.float32)]))
        observation, reward, done, info = env.step(action) # TODO Completes action, returns current chips, still alive