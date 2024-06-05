#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Mar 16,2024


noun_list = input("Enter nouns: ")

words = noun_list.split()
num_words = len(words)
num_plural = sum(word.endswith('s') for word in words)

print("Number of words:", num_words)
print("Fraction of your list that is plural is", num_plural / num_words if num_words > 0 else 0)












