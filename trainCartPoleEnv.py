from toyRF import *
from random import *

if __name__ == '__main__':
    N = 100
    init_params = [randint(0,1)*2-1 for i in range(4)]
    params =[]
    for i in range(0,N):
        epsilon = [gauss(0,1) for i in range(len(model.obs_dim()))]
        params.append(([init_params+epsilon],0))
        
    for i in range(0,N):
        model.CartPoleEnv.reset()
        model = LinearModel(params[i])
        new_obs, stopSignal, reward = model.CartPoleEnv.step(action)            
        action = model.action(new_obs)

        sorted(params,key=lambda parameter:parameter[1])
        model.param += float(sum(params[:int(100*rho)])/float(100*rho))
