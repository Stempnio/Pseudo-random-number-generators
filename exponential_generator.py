from myImports import *
import J_generator

def drawNumbers(n, a, m, c, x0, _lambda):
    arr = J_generator.drawNumbers(n, a, m, c, x0)
    for i in range(n):
        arr[i] = -np.log(arr[i]) / _lambda

    return arr

def plot(n, a, m, c, x0, _lambda):
    arr = drawNumbers(n, a, m, c, x0, _lambda)
    plt.style.use('ggplot')
    label = "lambda = {}".format(_lambda)
    plt.hist(arr, density=True, bins=int(n / 10), label=label, color="blue", alpha=0.5, )
    plt.title("Probability density function (Exponential)")
    plt.legend()
    plt.show()

def test(n, a, m, c, x0, _lambda):
    arr = drawNumbers(n, a, m, c, x0, _lambda)
    bins = 6
    hist1, edges = np.histogram(arr, bins=bins)

    hist2 = np.zeros(bins)
    hist2[0] = n*(1-np.exp(-_lambda*edges[1]))
    for i in range(1, bins):
        hist2[i] = n*((1-np.exp(-_lambda*edges[i+1]))-(1-np.exp(-_lambda*edges[i])))

    print("Liczby z rozkladu wykladniczego:")
    print(arr)
    fileSave(arr, hist1, hist2, "W", (bins-1))
    return arr
