//joseph freeman
//joseph.freeman41@myhunter.cuny.edu
//May 8, 2024

#include <iostream>

int main() {
    int num;
    std::cout << "Enter a number: ";
    std::cin >> num;

    // Check if the number is negative
    bool isNegative = num < 0;

    // If negative, convert to positive by adding 32
    if (isNegative) {
        num = 32 + num;
    }

    // Print 1 if negative, 0 if positive
    std::cout << (isNegative ? "1" : "0");

    // Start from 16 and halve each time
    int b = 16;

    // Iterate until b is greater than 0.5
    while (b > 0.5) {
        // Check if num is greater than or equal to b
        if (num >= b) {
            std::cout << "1";
            // Reduce num by b
            num -= b;
        } else {
            std::cout << "0";
        }
        // Halve b
        b /= 2;
    }

    // Print a new line
    std::cout << std::endl;

    return 0;
}
