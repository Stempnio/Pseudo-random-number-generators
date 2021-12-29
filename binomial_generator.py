from scipy.special import comb
from myImports import *
import bernoulli_generator


def drawNumbers(n, a, m, c, x0, p, numberOfBernoulliTrials):
    arr = np.zeros(n)
    lastValue = x0
    for i in range(n):
        arr[i] = np.count_nonzero(B_generator.drawNumbers(numberOfBernoulliTrials, a, m, c, lastValue, p) == 1)
        for i in range(n):
            lastValue = (a * lastValue - c) % m

    return arr

def plot(n, a, m, c, x0, p, numberOfBernoulliTrials):
    arr = drawNumbers(n, a, m, c, x0, p, numberOfBernoulliTrials)
    plt.style.use('ggplot')
    label = "n = {}, p = {}".format(numberOfBernoulliTrials, p)
    plt.hist(arr, bins=numberOfBernoulliTrials, color="blue", alpha=0.5, label=label, density=True)
    plt.title("Probability mass function (Binomial)")
    plt.legend()
    plt.show()


def test(n, a, m, c, x0, p, numberOfBernoulliTrials):
    arr = drawNumbers(n, a, m, c, x0, p, numberOfBernoulliTrials)
    bins = numberOfBernoulliTrials
    hist1, edges = np.histogram(arr, bins=bins)
    nums = np.sum(hist1)
    hist2 = np.zeros(numberOfBernoulliTrials)
    for i in range(numberOfBernoulliTrials):
        nCk = comb(numberOfBernoulliTrials,i)
        pi = p**i
        pi2 = (1-p)**(numberOfBernoulliTrials-i)
        hist2[i] = nums*nCk*pi*pi2

    print("Numbers from binomial distribution:")
    print(arr)
    fileSave(arr, hist1, hist2, "D", (bins-1))
    return arr
