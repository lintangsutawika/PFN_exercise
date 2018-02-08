from toyRF import LinearModel
from random import *
import sys

model = LinearModel([randint(0,1)*2-1 for i in range(4)])

obs = [randint(0,1)*2-1 for i in range(4)]
print(model.action(obs))
