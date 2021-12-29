from myImports import *
import J_generator

def drawNumbers(n,a,m,c,x0, _lambda):
    randomNums = J_generator.drawNumbers(n*n, a, m, c, x0)
    result = np.zeros(n)
    iter=0
    for i in range(n):
        x=0
        p=1
        p = p*randomNums[iter]
        iter += 1
        while p >= np.exp(-(_lambda)):
            p = randomNums[iter] * p
            iter += 1
            x += 1

        result[i] = x

    return result

def plot(n,a,m,c,x0, _lambda):
    arr = drawNumbers(n,a,m,c,x0, _lambda)
    plt.style.use('ggplot')
    heights, bins = np.histogram(arr, bins=25)
    heights = heights / sum(heights)
    label = "lambda = {}".format(_lambda)
    plt.bar(bins[:-1], heights, width=(max(bins) - min(bins)) / len(bins), color="blue", alpha=0.5, label=label)
    plt.title("Probability mass function (poisson)")
    plt.legend()
    plt.show()

def test(n,a,m,c,x0, _lambda):
    arr = drawNumbers(n, a, m, c, x0, _lambda)
    bins = np.arange(0,10,1)
    hist1, edges = np.histogram(arr, bins=bins)
    print(edges)
    hist2 = np.zeros(len(hist1))
    for i in range(0, len(hist1)):
        hist2[i] = n*(np.exp(-_lambda)*(_lambda**edges[1])/np.math.factorial(edges[i]))


    print("numbers with Poisson distribution:")
    print(arr)
    fileSave(arr, hist1, hist2, "P", (len(bins)-1))
    return arr
