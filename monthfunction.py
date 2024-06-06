#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Apr 3,2024



def monthString(monthNum):
    """
    Takes as input a number, monthNum, and
    returns the corresponding month name as a string.
    Example: monthString(1) returns "January".
    Assumes that input is an integer ranging from 1 to 12
    """
    monthString = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    return monthString.get(monthNum, "Wrong month")

def main():
    n = int(input('Enter number of the month: '))
    mString = monthString(n)
    print('The month is', mString)

# Allow script to be run directly:
if __name__ == "__main__":
    main()

