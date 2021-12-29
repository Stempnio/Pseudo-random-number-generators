from myImports import *
import J_generator
from scipy.stats import norm

def drawNumbers(n, a, m, c, x0):
    arr = J_generator.drawNumbers(n,a,m,c,x0)
    U1 = arr[0:int(n/2)-1]
    # we want U1 and U2 to be equal size
    max = n
    if max % 2 != 0:
        max -= 1
    U2 = arr[int(n/2):max-1]

    Z1 = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)
    Z2 = np.sqrt(-2*np.log(U1))*np.sin(2*np.pi*U2)

    return Z2

def plot(n, a, m, c, x0):
    arr = drawNumbers(n, a, m, c, x0)
    mean = np.mean(arr)
    std = np.std(arr)

    plt.style.use('ggplot')
    label = "mean = {}, std = {}".format((round(mean, 4)), (round(std, 3)))
    #
    x = np.arange(np.min(arr),np.max(arr), 0.01)
    plt.plot(x, norm.pdf(x,mean,std))
    #
    plt.hist(arr, density=True, bins=100, label=label, color="blue", alpha=0.5, )
    plt.title("Probability density function (Normal)")
    plt.legend()
    plt.show()

def test(n, a, m, c, x0):
    arr = drawNumbers(n, a, m, c, x0)

    bins = np.arange(-3,4,1)
    hist1, bin_edges = np.histogram(arr, bins=bins)

    # CALCULATED WITH "https://keisan.casio.com/exec/system/14060744929691", mean = 0.0189, std = 0.99
    hist2 = np.zeros(6)
    hist2[0] = 0.019563882541099 # [-3;-2]
    hist2[1] = 0.13098434895595 # [-2;-1]
    hist2[2] = 0.34068954239221
    hist2[3] = 0.34677538419698
    hist2[4] = 0.13815011539693
    hist2[5] = 0.021389173567845 # [2;3]
    hist2 *= np.sum((-3 <= arr) & (arr <= 3))

    print("numbers with a normal distribution:")
    print(arr[:100])
    fileSave(arr, hist1, hist2, "N", (len(bins)-1))
    return arr

