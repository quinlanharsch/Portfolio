import robby
import numpy as np
import numpy.random as r

## Globals ##

population_size = 200
number_children = population_size
tournament_size = int(population_size/20)
genome_length = 243
crossover_rate = 1.0
mutation_rate = 0.005
ap_cleaning_session = 200
num_generations = 500
can_density = 0.5
simulation_sessions = 10

rw = robby.World(10, 10)
rw.distributeCans(0.5)
rw.goto(0,0)
rw.graphicsOff()
rw.graphicsEnabled = False


def initialize_population():
    return r.choice(7,(population_size, genome_length))


def parent_selection(population, n, k):
    '''Tournament selection (size k) of n parents from a given SORTED population.'''
    x = r.randint(population.shape[0], size=(n,k))
    indices = x.min(axis=1)
    return population[indices,:]


def crossover(parents):
    children = []
    for i in range(number_children-1):
        parent_1 = parents[i]
        parent_2 = parents[i + 1]
        if r.rand() < crossover_rate:
            crossover_point = r.choice(genome_length)
            child_1 = np.r_[parent_1[:crossover_point],parent_2[crossover_point:]]
            child_2 = np.r_[parent_2[:crossover_point],parent_1[crossover_point:]]
        else:
            child_1 = parent_1
            child_2 = parent_2
        children.append(child_1)
        children.append(child_2)
    return np.array(children)


def mutation(pop):
    for ix, iy in np.ndindex(pop.shape):
        if r.rand() < mutation_rate:
            pop[ix,iy] = r.choice(7)
    return pop


def survivor_selection(parents, parent_fitnesses, children, elite):
    children_parents = np.r_[parents, children]
    child_parent_fitnesses = np.r_[parent_fitnesses, fitness(children)]
    children_parents = fitness_sort(children_parents, child_parent_fitnesses)
    return np.vstack((
        elite,
        children_parents[:population_size-1]
    ))


def fitness(pop):
    fits = []
    for x in pop:
        rewards = 0
        for i in range(simulation_sessions):
            rewards += rw.simulate("".join([str(int(i)) for i in x]))
        fits.append(rewards/simulation_sessions)
    return np.array(fits)


def fitness_sort(pop, fits):
    return pop[np.argsort(-fits)]


population = initialize_population()
best_f = np.empty((num_generations))
avg_f = np.empty((num_generations))
for i in range(num_generations):
    fitnesses = fitness(population)
    elite = population[np.argmax(fitnesses)]

    best_f[i] = np.max(fitnesses)
    avg_f[i] = np.average(fitnesses)
    print("Generation: "+str(i), "Best:"+str(best_f[i]), "Average:"+str(avg_f[i]),sep="\n")
    print("Best Strategy:", "".join([str(int(i)) for i in population[np.argmax(fitnesses)]]),"\n")

    population = fitness_sort(population, fitnesses)
    parents = parent_selection(population, number_children, tournament_size)
    children = mutation(crossover(parents))
    population = survivor_selection(parents, fitnesses, children, elite)
