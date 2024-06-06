//joseph freeman
//joseph.freeman41@myhunter.cuny.edu
//Apr 24, 2024


#include <iostream>

int main() {
    int year;
    do {
        std::cout << "Enter year: ";
        std::cin >> year;
        if (year > 2018) {
            std::cout << "Year must be 2018 or earlier" << std::endl;
        }
    } while (year > 2018);

    std::cout << "You entered: " << year << std::endl;

    return 0;
}







