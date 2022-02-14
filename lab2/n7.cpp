#include <iostream>
#include <cstdlib> // для system
using namespace std;

void print_binary(unsigned long long value){
    if (value > 1){
        print_binary(value / 2);
    }
    cout << value % 2;
}

int main() {
    unsigned long long n;
    cin >> n;
    print_binary(n);
    return 0;
}