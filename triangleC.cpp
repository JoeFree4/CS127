//joseph freeman
//joseph.freeman41@myhunter.cuny.edu
//Apr 24, 2024



#include <iostream>

int main() {
    int height;
    std::cout << "Enter a number: ";
    std::cin >> height;

    for (int i = 1; i <= height; ++i) {
        for (int j = 0; j < i; ++j) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }

    return 0;
}





