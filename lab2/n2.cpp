#include <iostream>
#include <cstdlib> // для system
#include <cassert>
#include <cmath>
using namespace std;

void clean(){
    char c;
    while (cin >> c && c!= '@'){
        if ('0' <= c && c <= '9'){
            int d = c - '0';
            cout << d;
        }
    }
}

int main() {
    clean();
    return 0;
}