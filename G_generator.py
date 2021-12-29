from myImports import *

def drawNumbers(n, a, m, c, x0):
    arr = np.zeros(n)
    arr[0] = x0
    for i in range(1, n):
        arr[i] = (a * arr[i - 1] - c) % m
    return arr

def test(n, a, m, c, x0):
    arr = drawNumbers(n, a, m, c, x0)
    bins=8
    hist1, edges = np.histogram(arr, bins=bins)
    hist2 = np.zeros(bins)
    for i in range(bins):
        hist2[i] = 1/bins * n

    print("Uniformly distributed numbers from the G generator: ")
    print(arr)
    fileSave(arr, hist1, hist2, "G", (bins-1))
    return arr
