from myImports import *
import binomial_generator
import normal_generator
import poisson_generator
import exponential_generator
import G_generator
import uniform_generator
import bernoulli_generator


np.set_printoptions(suppress=True)

a = 7 ** 5
m = 2 ** 31 - 1
c = 1013904223
# x0 = 6 ** 8 - 1
x0 = 55484267
p = 0.7
n = 100

#Uniform distribution
G_generator.test(n,a,m,c,x0)


#Uniform distribution (0;1)
uniform_generator.plot(n,a,m,c,x0)
uniform_generator.test(n,a,m,c,x0)


#Bernoulli distribution
n = 10000
bernoulli_generator..plot(n,a,m,c,x0,p)
bernoulli_generator..test(n,a,m,c,x0,p)


# Binomial distribution
trials = 10
n = 5000
p=0.5
binomial_generator.plot(n, a, m, c, x0, p, trials)
binomial_generator.test(n, a, m, c, x0, p, trials)


#Poisson distribution
n = 1000
_lambda = 1
poisson_generator.plot(n, a, m, c, x0, _lambda)
poisson_generator.test(n, a, m, c, x0, _lambda)


# Exponential distribution (inverse transform sampling)
n = 1000
_lambda = 1
exponential_generator.plot(n, a, m, c, x0, _lambda)
exponential_generator.test(n, a, m, c, x0, _lambda)


# Normal distribution (box-Muller Transform)
n = 10000
normal_generator.plot(n, a, m, c, x0)
normal_generator.test(n, a, m, c, x0)
