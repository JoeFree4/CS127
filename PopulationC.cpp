//joseph freeman
//joseph.freeman41@myhunter.cuny.edu
//May 10,2024

#include <iostream>
using namespace std;

int main() {
    double B = 12.4 / 1000; // birth rate
    double D = 8.4 / 1000;   // death rate
    double p = 325.7;       // initial population (in millions)

    int years;
    cout << "Enter the number of years: ";
    cin >> years;

    cout << "Year\tPopulation (millions)" << endl;
    for (int i = 0; i <= years; i++) {
        cout << 2017 + i << "\t" << p << endl;
        p = p + p * B - p * D;
    }

    return 0;
}

