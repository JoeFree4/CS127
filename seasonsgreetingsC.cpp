//joseph freeman
//joseph.freeman41@myhunter.cuny.edu
//Apr 24, 2024



#include <iostream>

int main() {
    int month;
    std::cout << "Enter month (as a number): ";
    std::cin >> month;

    if (month < 3 || month > 11) {
        std::cout << "Happy Winter" << std::endl;
    } else if (month >= 3 && month < 7) {
        std::cout << "Happy Spring" << std::endl;
    } else if (month >= 7 && month < 9) {
        std::cout << "Happy Summer" << std::endl;
    } else {
        std::cout << "Happy Fall" << std::endl;
    }

    return 0;
}






