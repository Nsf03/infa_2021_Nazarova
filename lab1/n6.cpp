
#include <iostream>
#include <cstdlib> // для system
using namespace std;

int main() {
    int max, max_now;
    max = 0;
    max_now = 1;
    long first, second;
    if (cin >> first) {
        max = 1;
    }
    while (cin >> second){
        if (second > first) {
            max_now += 1;
        } else {
            max_now = 1;
        }
        if (max_now > max){
            max = max_now;
        } first = second;

    }
    cout << max;
    return 0;
}
