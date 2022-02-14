#include <iostream>
#include <cstdlib> // для system
#include <cassert>
#include <cmath>
using namespace std;

unsigned long long read_num(){
    unsigned long long value;
    cin >> value;
    return value;
}

bool is_dev(unsigned long long value, unsigned long long i){
    if (value%i == 0){
        return true;
    } else{
        return false;
    }
}

bool is_prime(unsigned long long value){
    if (value == 1){
        return false;
    }
    if (value == 2){
        return true;
    }
    for (unsigned long long i = 2; i < sqrt(value)+1; i++){
        if (is_dev(value, i) == true){
            return false;
        }
    }
    return true;
}

void answer(bool i){
    if(i == true){
        cout << "YES";
    }else{
        cout << "NO";
    }
}

int main() {
    assert(is_prime(896566423) == true);
    assert(is_prime(1) == false);
    assert(is_prime(896566424) == false);
    auto a = read_num();
    answer(is_prime(a));
    return 0;
}