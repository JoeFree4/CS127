#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Mar 8, 2024

import matplotlib.pyplot as plt
import numpy as np

addfile = input("Enter file name: ")

ca = plt.imread(addfile)
countSnow = 0
t = 0.75

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):

        if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
            countSnow = countSnow + 1

print("Snow count is", countSnow)
