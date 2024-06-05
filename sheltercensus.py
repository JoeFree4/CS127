#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Mar 25,2024


import matplotlib.pyplot as plt
import pandas as pd


report = input("enter file name of input file: ")
output = input("enter name of output file: ")

homeless = pd.read_csv(report)

homeless['Fraction Children'] = homeless["Total Children in Shelter"]/homeless["Total Individuals in Shelter"]

homeless.plot(x = "Date of Census", y = "Fraction Children")

fig = plt.gcf()
fig.savefig(output)
