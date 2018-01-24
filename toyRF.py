from random import *

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

    def reset(self, states):
        print('r obs {} {} {} {}'.format())
        sys.stdout.flush()
        self.resetState = randint(0,1)*2-1
        self.resetFlag = 1
        self.stepNum = 0
        return self.resetState

    def obs_dim(self):
        return 1

    def step(self, action):
        print('s {}'.format(action))
        if self.stepNum >= 500:
            stopSignal = 1
            self.stepNum = 0
        else:
            stopSignal = 0
            self.stepNum += 1

        if self.resetFlag == 1:
            prev_obs = self.resetState
            self.resetFlag = 0
        else:
            prev_obs = self.new_obs  

        self.new_obs = randint(0,1)*2-1
        reward = 1
        return [self.new_obs, stopSignal, reward]

    def test(self):
        pass

class LinearModel(object):
    """docstring for LinearModel"""
    def __init__(self, init_param):
        self.model = init_param
        
    def action(self, obs):
        innerProduct = 0
        for element in len(obs):
            innerProduct = innerProduct + self.model[element]*obs[element]

        return 1 if innerProduct > 0 else -1

if __name__ == '__main__':
    env = EasyEnv()