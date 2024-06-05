#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Mar 8, 2024

#this program allows the user to input the hours left until the weekend and outputs the days and hours leftover
hours = int(input("Number of hours until the weekend: "))
days = hours//24
leftover = hours%24

print("Days: ", days)
print("Hours: ", leftover)
