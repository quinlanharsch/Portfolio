import numpy as np
import numpy.random as r
import matplotlib.pyplot as plt


mu = 300  # population size

n = 50  # number of x variables per individual (used in fitness function)
r_x = (-30, 30)  # range of values the x variables can take

m = 1  # number of sigma variables per individual
r_s = (0.1, 10)  # range of sigma values

m_mu = 0  # mu value for x' = x + N(mu, s) in mutation
c_size = 500  # number of children (!!! Must be greater than mu, b/c of (mu, l))
termination = 1000  # 10000


def initialize():
    x = r.uniform(r_x[0], r_x[1], (mu, n))
    s = r.uniform(r_s[0], r_s[1], (mu, m))
    return np.hstack((x,s))


def fitness(p, sz):  # note: can be run with {x,s} or {x}
     fits = []
     for i in range(sz):
         fits.append(np.sum(p[i,:n]))
     return np.array(fits)


#   parent selection (uniform selection) in crossover
def crossover(p) -> object:
    x, s = p[:, :n], p[:, n:]  # split parents into X and S
    children = []
    for i in range(c_size):
        parents = x[r.choice(n,size=2,replace=False)]  # choose 2 Xs
        x_fit = fitness(parents, 2)
        if x_fit[0] < x_fit[1]: sel_x = x[0]  # pick the best (########HIGHEST fitness)
        else: sel_x = x[1]

        sigs = s.ravel()[r.choice(mu,size=2,replace=False)]  # pick two Ss
        sel_s = np.average(sigs)  # average them

        children.append(np.hstack((sel_x,sel_s)))
    return np.array(children)


def mutation(p):
    x, s = p[:,:n], p[:,n:]  # split parents into X and S

    # sigma mutation by *= e^N(0,tau)
    tau = 1 / np.sqrt(2 * np.sqrt(n))
    s = np.dot(s, np.exp(r.normal(0, tau, size=m)))
    for i in np.nditer(s, op_flags=['readwrite']):  # check out of bounds
        if i[...] < r_s[0]: i[...] = r_s[0]
        if i[...] > r_s[1]: i[...] = r_s[1]

    # x mutation by += N(mu, s)
    x = np.add(x, r.normal(0, s)[:,None])
    for j in np.nditer(s, op_flags=['readwrite']):  # check out of bounds
        if j[...] < r_x[0]: j[...] = r_x[0]
        if j[...] > r_x[1]: j[...] = r_x[1]
    return np.column_stack((x, s))  # child


def survivors(children): return sort(children)[:mu]  #### changed sorting direction


def sort(a): return a[np.argsort(fitness(a, a.shape[0]))]


# r.seed(4)
pop = initialize()
best_fits = [np.infty]
avg_fits = [np.infty]

generation = 1
while generation <= termination:

    fits = fitness(pop, mu)
    best_fits.append(np.max(fits))
    avg_fits.append(np.average(fits))

    children = mutation(crossover(pop))
    pop = survivors(children)

    print("Gen:", generation, " \tBest fitness:", best_fits[0])
    generation += 1

np.set_printoptions(threshold=np.inf)
print(sort(pop)[0])

plt.plot(np.arange(1, len(best_fits)), best_fits[1:], label='Best')
plt.plot(np.arange(1, len(avg_fits)), avg_fits[1:], label='Average')
plt.legend()
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.show()