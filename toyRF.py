from random import *
import sys

class EasyEnv:
    def __init__(self):
        self.prev_obs = 0
        self.resetState = 0
        self.resetFlag = 0
        self.stepNum = 0
        self.new_obs = 0

    def reset(self):
        self.resetState = randint(0,1)*2-1
        self.resetFlag = 1
        self.stepNum = 0
        return self.resetState

    def obs_dim(self):
        return 1

    def step(self, action):
        if self.stepNum >= 10:
            stopSignal = 1
            self.stepNum = 0
            sys.exit("Environment ends")

        else:
            stopSignal = 0
            self.stepNum += 1

        if self.resetFlag == 1:
            prev_obs = self.resetState
            self.resetFlag = 0
        else:
            prev_obs = self.new_obs  

        self.new_obs = randint(0,1)*2-1
        reward = action * prev_obs
        
        return [self.new_obs, stopSignal, reward]
        
    def test(self):
        pass

class CartPoleEnv(object):
    def __init__(self):
        self.prev_obs = 0
        self.resetState = 0
        self.resetFlag = 0
        self.stepNum = 0
        self.new_obs = 0

    def reset(self):
        print('r')
        sys.stdout.flush()

        # receive initial observation
        feedback = input()
        feedback = feedback.split()
        sys.stderr.write('Reset: {}\n'.format(feedback))

        self.resetState = feedback
        self.resetFlag = 1
        self.stepNum = 0
        return self.resetState

    def obs_dim(self):
        return 4

    def step(self, action):
        sys.stdout.flush()
        action = randint(0, 1) * 2 - 1
        print('s {}'.format(action))
        sys.stdout.flush()

        # receive observation after the action
        feedback = input()
        feedback = feedback.split()
        # sys.stderr.write('{}\n'.format(feedback))

        if feedback[0] == 'done':
            sys.stderr.write('{}\n'.format(feedback))
            sys.exit()
            pass

        if self.stepNum >= 500:
            stopSignal = 1
            self.stepNum = 0
            print('q')
            sys.stdout.flush()

        else:
            stopSignal = 0
            self.stepNum += 1

        if self.resetFlag == 1:
            prev_obs = self.resetState
            self.resetFlag = 0
        else:
            prev_obs = self.new_obs  

        self.new_obs = feedback[1:]
        reward = 1
        return [self.new_obs, stopSignal, reward]

    def test(self):
        pass

class LinearModel(object):
    """docstring for LinearModel"""
    def __init__(self, init_param):
        self.param = init_param
        self.CartPoleEnv = CartPoleEnv()

    def action(self, obs):
        innerProduct = 0
        for element in range(len(obs)):
            innerProduct = innerProduct + self.param[element]*obs[element]
        
        return 1 if innerProduct > 0 else -1

    def obs_dim(self):
        4

if __name__ == '__main__':
    env = EasyEnv()