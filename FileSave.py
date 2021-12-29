from ChiSquare import chiSquareValue
import numpy as np

def fileSave(arr, hist1, hist2, type, dof):
    f = open("out/{}_generator.txt".format(type), "w")
    f.write("The value of the chi-square statistic: ")
    chi = chiSquareValue(hist1, hist2)
    f.write(str(chi))

    f.write("\nDegrees of freedom: ")\

    f.write(str(dof))

    f.write("\n\n")
    f.write(np.array_str(arr[:100]))

    f.close()