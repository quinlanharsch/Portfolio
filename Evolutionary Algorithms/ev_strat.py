# Quinlan Harsch    Evolution Strategies
# ######################################################################################################################

# ### Imports ##########################################################################################################
import numpy as np
import numpy.random as r

# ### Globals ##########################################################################################################
mu = 2
n = 3
r_x = (0, 10)
r_s = (0.1, 10)


# ### Functions ########################################################################################################
def init(mu, n, r_x, r_s):
    x = r.uniform(r_x[0], r_x[1], (mu, n))
    s = r.uniform(r_s[0], r_s[1], (mu))
    return np.column_stack((x,s))


def fit(pop):
    f = []
    for indv in pop:
       f.append((indv[0] - 5)**8 + (indv[1] - 7)**10 + (indv[2] - 2)**4)
    return np.array(f)


def mutation(p):
    x, s = p[:n], p[n:] # parent

    #t
    tau_p = 1 / np.sqrt(2 * n)
    tau = 1 / np.sqrt(2 * np.sqrt(n))
    nc = r.normal(0, tau_p)
    s *= np.exp(nc) + r.normal(0, tau)
    for m in s:
        if m < r_s[0]: m = r_s[0]
        if m > r_s[1]: m = r_s[1]

    #x
    x += r.normal(0,s,n)
    for m in x:
        if m < r_x[0]: m = r_x[0]
        if m > r_x[1]: m = r_x[1]

    return np.hstack((x,s)) #child


def sel(p, c, fits):
    if fits[0] > fits[1]:
        return p
    return c


# ### Body #############################################################################################################
pop = init(mu, n, r_x, r_x)

fits = [np.Inf, np.Inf]
while fits[0] != 0:
    p = pop[0]
    c = mutation(p)
    fits = fit(np.vstack((p,c)))
    print("Fitnesses",fits[0],"Population", p, sep='\n')
    pop[0] = sel(p, c, fits)