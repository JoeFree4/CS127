#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Mar 22, 2024

import matplotlib.pyplot as plt
import pandas as pd

userdata = input("enter borough name: ")
outdata = input("enter output file name: ")

pop = pd.read_csv('nycHistPop.csv', skiprows=5)

pop["Fraction"] = pop[userdata]/pop["Total"]

pop.plot(x = "Year", y = "Fraction")

fig = plt.gcf()

fig.savefig(outdata)


