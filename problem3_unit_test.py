from toyRF import LinearModel
from random import *
import sys

model = LinearModel([randint(0,1)*2-1, randint(0,1)*2-1, randint(0,1)*2-1, randint(0,1)*2-1])

obs = [randint(0,1)*2-1, randint(0,1)*2-1, randint(0,1)*2-1, randint(0,1)*2-1]
print(model.action(obs))
