#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Mar 22, 2024

import matplotlib.pyplot as plt
import pandas as pd

userdata = input("enter borough name: ")


pop = pd.read_csv('nycHistPop.csv', skiprows=5)


average = pop[userdata].mean()
maxpop = pop[userdata].max()



print("Average population: ", average)
print("Maximum population: ", maxpop)
