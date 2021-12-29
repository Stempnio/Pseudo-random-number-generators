import numpy as np

import ChiSquare
from myImports import *
import uniform_generator

def drawNumbers(n, a, m, c, x0, p):
    numbersZeroOne = J_generator.drawNumbers(n, a, m, c, x0)
    arr = np.zeros(n)

    for i in range(0, n):
        if numbersZeroOne[i] < p:
            arr[i] = 1

    return arr

def plot(n,a,m,c,x0,p):
    arr = drawNumbers(n,a,m,c,x0, p)
    plt.style.use('ggplot')
    label = "p = {}".format(p)
    plt.hist(arr, density=True, color="blue", alpha=0.5, label=label)
    plt.legend()
    plt.title("Probability mass function (Bernoulli)")
    plt.show()

def test(n,a,m,c,x0,p):
    arr = drawNumbers(n, a, m, c, x0, p)
    bins=2
    hist1, edges = np.histogram(arr, bins=bins)
    hist2 = np.zeros(2)
    hist2[0] = n*(1-p)
    hist2[1] = n*p

    print("Numbers from Bernoulli distribution:")
    print(arr[:100])
    fileSave(arr, hist1, hist2, "B", (bins-1))
    return arr
