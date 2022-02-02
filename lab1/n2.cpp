#include <iostream>
#include <cstdlib> // для system
using namespace std;

int main() {
    int n;
    cin >> n;
    for (unsigned int i = 0; i < n; i++) {
        if (n % 5 == 0) {
            cout << "@";
        } else
            cout << "%";
    }
    return 0;
}