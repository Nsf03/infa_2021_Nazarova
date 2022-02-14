
#include <iostream>
#include <cstdlib> // для system
#include <cassert>
#include <cmath>
using namespace std;

unsigned long long fib(unsigned int n){
    unsigned long long next = 1;
    unsigned long long now = 0;
    unsigned long long prev = 0;
    unsigned int count = 0;
    if (n == 1){
        return 0;
    } if (n == 2){
        return (1);
    }
    while (count < n-2){
        now = next + prev;
        prev = next;
        next = now;
        count += 1;
    }
    return next;
}

int main() {
    unsigned int n;
    cin >> n;
    cout << fib(n);
    return 0;
}