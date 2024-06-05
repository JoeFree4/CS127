#joseph freeman
#joseph.freeman41@myhunter.cuny.edu
#Apr 1,2024

def computeFare(zone, ticket_type):
    fare_table = {
        1: {"peak": 8.75, "off-peak": 6.25},
        2: {"peak": 10.25, "off-peak": 7.50},
        3: {"peak": 10.25, "off-peak": 7.50},
        4: {"peak": 12.00, "off-peak": 8.75},
        5: {"peak": 13.50, "off-peak": 9.75},
        6: {"peak": 13.50, "off-peak": 9.75},
        7: {"peak": 13.50, "off-peak": 9.75}
    }
    
    if zone <= 7:
        return fare_table[zone].get(ticket_type, -1)
    else:
        return -1

def main():
    user_zone = int(input('Enter the number of zones: '))
    user_ticket = input('Enter the ticket type (peak/off-peak): ')

    fare = computeFare(user_zone, user_ticket)
    if fare < 0:
        print("Invalid input: Zone is greater than 7")
    else:
        print('The fare is:', fare)

if __name__ == '__main__':
    main()

