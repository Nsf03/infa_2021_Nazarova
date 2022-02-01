#include <iostream>
#include <cstdlib> // для system
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n % 5 == 0) {
        for (unsigned int i = 0; i < n; i++) {
            cout << "@";
        }
    } else {
        for (unsigned int i = 0; i < n; i++) {
            cout << "%";
        }
    }
    return 0;
}