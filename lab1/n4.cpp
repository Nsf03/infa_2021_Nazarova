
#include <iostream>
#include <cstdlib> // для system
using namespace std;

int main() {
    int min;
    min = 100;
    unsigned int n;
    cin >> n;
    for (unsigned int i = 0; i < n; i++) {
        long value;
        cin >> value;
        if (value < min) {
            min = value;
        }
    }
    cout << min;
    return 0;
}