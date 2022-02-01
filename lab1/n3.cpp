#include <iostream>
#include <cstdlib> // для system
using namespace std;

int main() {
    int x, y, pr;
    pr = 1;
    cin >> x >> y;
    for (int i = 0; i < y; i++) {
        pr = pr * x;
    }
    cout << pr;
    return 0;
}