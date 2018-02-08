from toyRF import *
from random import *

if __name__ == '__main__':
    N = 100
    init_params = [randint(0,1)*2-1 for i in range(4)]
    params =[]
    for i in range(N):
        epsilon = [gauss(0,1) for i in range(len(model.obs_dim()))]
        params.append(init_params+epsilon)
        
    for i in range(N):
        model.CartPoleEnv.reset()
        model = LinearModel(params[i])
        new_obs, stopSignal, reward = model.CartPoleEnv.step(action)            
        action = model.LinearModel.action(new_obs)
