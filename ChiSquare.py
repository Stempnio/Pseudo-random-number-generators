def chiSquareValue(observed, expected):
    if(len(observed) != len(expected)):
        print("Arrays of different sizes!!")
        return -1

    result=0
    n = len(observed)
    for i in range(n):
        result += (observed[i]-expected[i])**2 / expected[i]

    print("the value of chi-square statistic:", result)
    return result