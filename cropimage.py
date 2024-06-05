#Joseph Freeman
#joseph.freeman41@myhunter.cuny.edu
#Mar 5, 2024


import matplotlib.pyplot as plt
import numpy as np

inF = input("Enter file name: ")
outputfile = input("output file name: ")

img = plt.imread(inF) #read an imge from inF

height = img.shape[0] #Get height
width = img.shape[1]  #Get width

img2 = img[height//2:, :width//2] #crop to the lower left corner, image slicing


plt.imsave(outputfile, img2)
