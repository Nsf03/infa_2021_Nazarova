#include <iostream>
#include <cstdlib> // для system
#include <cassert>
#include <cmath>
using namespace std;

bool reset_num = false;
bool is_dev(unsigned int value, unsigned int i){
    if (value%i == 0){
        return true;
    } else{
        return false;
    }
}
bool is_prime(unsigned int value){
    if (value == 1){
        return false;
    }
    if (value == 2){
        return true;
    }
    for (unsigned int i = 2; i < sqrt(value)+1; i++){
        if (is_dev(value, i) == true){
            return false;
        }
    }
    return true;
}

unsigned int next_prime(){
    static unsigned int now_prime = 1;
    if (::reset_num == true){
        now_prime = 1;
    }
    unsigned int now_num = now_prime + 1;
    while(is_prime(now_num) == false){
        now_num += 1;
    }
    now_prime = now_num;
    ::reset_num = false;
    return(now_prime);
}
void print_int(int value){
    cout << value << endl;
}
void start_reset(){
    char i;
    while(cin >> i){
        if (i == '!'){
            ::reset_num = true;
        }
        print_int(next_prime());
    }
}


int main() {
    cout << "Ane symbol - new prime. ! - reset";
    start_reset();
    return 0;
}