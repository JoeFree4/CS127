#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Mar 11, 2024

import matplotlib.pyplot as plt
import numpy as np


userInput = input("Enter size of image: ")
file_name = input("Enter output file: ")

blank = np.ones((int(userInput), int(userInput), 3))

for row in range(int(userInput)):
    for col in range(int(userInput)):
        if row % 2 == 0:
            blank[row,col,0] = 1.0
            blank[row,col,1] = 0
            blank[row,col,2] = 1.0
        else:
            blank[row,col,0] = 1.0
            blank[row,col,1] = 1.0
            blank[row,col,2] = 0
            
            


plt.imsave(file_name, blank)
