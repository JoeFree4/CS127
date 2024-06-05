#joseph freemasn
#joseph.freeman41@myhunter.cuny.edu
#Mar 30,2024



inputnames = input("Please enter your list of names: ")


names_split = inputnames.split('; ')

print("You entered: ")


for name in names_split:
    
    last_name, first_name= name.split(', ')
    
    print(first_name, last_name)

print("Thank you for using my name organizer!")
