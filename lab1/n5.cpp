
#include <iostream>
#include <cstdlib> // для system
using namespace std;

int main() {
    int min, min_ost;
    min_ost = 101;
    long value;
    while (cin >> value){
        if (value % 101 < min_ost){
            min_ost = value % 101;
            min = value;
        }
    }
    cout << min;
    return 0;
}