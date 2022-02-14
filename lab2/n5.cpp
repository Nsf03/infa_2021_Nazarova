
#include <iostream>
#include <cstdlib> // для system
#include <cassert>
using namespace std;

unsigned long long factorial(unsigned int n){
    if (n == 0){
        return(1);
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    unsigned int n;
    cin >> n;
    cout << factorial(n);
    return 0;
}