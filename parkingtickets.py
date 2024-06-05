#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Mar 31,2024


import pandas as pd


enterfile = input("Enter file name: ")


enter_attribute = input("Enter attribute: ")


readtickets = pd.read_csv(enterfile)


alloffenders = readtickets[enter_attribute].value_counts().head(10)


print("The 10 worst offenders are:")
print(alloffenders)
