import ChiSquare
from myImports import *
import G_generator


def drawNumbers(n, a, m, c, x0):
    arr = G_generator.drawNumbers(n, a, m, c, x0)
    arr /= m
    return arr

def plot(n, a, m, c, x0):
    arr = drawNumbers(n, a, m, c, x0)
    plt.style.use('ggplot')
    heights, bins = np.histogram(arr, bins=n*n)
    heights = heights / sum(heights)
    label = "n: {}".format(n)
    plt.bar(bins[:-1], heights, width=(max(bins) - min(bins)) / n, color="blue", alpha=0.5, label=label)
    plt.title("Probability mass function (uniform)")
    plt.legend()
    plt.show()

def test(n, a, m, c, x0):
    arr = drawNumbers(n, a, m, c, x0)

    bins=8
    hist1, edges = np.histogram(arr, bins=bins)
    hist2 = np.zeros(bins)
    for i in range(bins):
        hist2[i] = 1/bins * n

    print("Uniformly distributed numbers (0;1): ")
    print(arr)
    fileSave(arr, hist1, hist2, "J", (bins-1))
    return arr