#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Apr 1,2024


import pandas as pd


file = input("Enter file name: ")

collisions = pd.read_csv(file)


contributingfactors = collisions['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().head(3)


print("Top three contributing factors for collisions:")
print(contributingfactors)
