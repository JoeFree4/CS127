#Joseph Freeman
#joseph.freeman41@myhunter.cuny.edu
#February 20,2024

firstWord = input("Enter a word: ")
newWord = ""

print("Your word in code is: ")
for i in firstWord:
    swapWord = chr(((ord(i) - ord('a') + 13) % 26) + ord('a'))
    newWord += swapWord

print(newWord)

#This program moves each letter to the right by 13 units
