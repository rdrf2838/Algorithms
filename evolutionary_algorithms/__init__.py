from numpy import random

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
import numpy as np
import array

X_START = -4
X_END = 4
X_STEP = 0.5


def unknown(x):
    return 1.3 * x + 1.9 * x ** 2 - 4.2 * x ** 3 + 5.0


def sample(inputs):
    return np.array([unknown(inp) + random.normal(5.) for inp in inputs])


X = np.array([x for x in np.arange(X_START, X_END, X_STEP)])
Y = sample(X)

data = list(zip(X, Y))

IND_SIZE = 5
NGEN = 100

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

creator.create("Individual", array.array, typecode="d", fitness=creator.FitnessMin, strategy=None)

creator.create("Strategy", array.array, typecode="d")


def generateES(ind_cls, strg_cls, size):
    ind = ind_cls(random.normal() for _ in range(size))
    ind.strategy = strg_cls(random.normal() for _ in range(size))
    return ind


toolbox = base.Toolbox()

# generation functions
toolbox.register("individual", generateES, creator.Individual, creator.Strategy, IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def pred(ind, x):
    y_ = 0.0

    for i in range(1, IND_SIZE):
        y_ += ind[i - 1] * x ** i

    y_ += ind[IND_SIZE - 1]

    return y_


def fitness(ind, data):
    mse = 0.0

    for x, y in data:
        y_ = pred(ind, x)
        mse += (y - y_) ** 2

    return mse / len(data),


toolbox.register("evaluate", fitness, data=data)

toolbox.register("mate", tools.cxESBlend, alpha=0.1)
toolbox.register("mutate", tools.mutESLogNormal, c=1.0, indpb=0.3)
toolbox.register("select", tools.selTournament, tournsize=3)

stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("std", np.std)
stats.register("min", np.min)
stats.register("max", np.max)
# ES params
MU, LAMBDA = 10, 100

hof = tools.HallOfFame(1)

pop = toolbox.population(n=MU)

pop, logbook = algorithms.eaMuCommaLambda(pop, toolbox, mu=MU, lambda_=LAMBDA,
            cxpb=0.6, mutpb=0.3, ngen=1, stats=stats, halloffame=hof, verbose=False)

print(hof)