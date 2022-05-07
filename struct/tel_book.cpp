
#include <iostream>
#include <fstream>
using namespace std;
struct Person{
    string name;
    unsigned long long tel;
    string email;
};
void find_with_tel(unsigned long long tel, Person* book, unsigned n){
    for (unsigned i=0; i<n; i ++){
        if (tel == book[i].tel){
            cout << book[i].name << " " << book[i].tel << " " << book[i].email;
            return;

        }
    }
    cout << "WRONG NUMBER!!!!!";
}
void find_with_name(string name, Person* book, unsigned n){
    for (unsigned i=0; i<n; i ++){
        if (name == book[i].name){
            cout << book[i].name << " " << book[i].tel << " " << book[i].email;
            return;

        }
    } cout << "WRONG NAME!!!!!";
}


int main(){
    ifstream F;
    F.open("book.txt");
    unsigned n;
    F >> n;
    Person* book = new Person[n];
    for (unsigned i=0; i<n; i++){
        F >> book[i].name >> book[i].tel >> book[i].email;
    }
    F.close();
    cout << "Search by number - T, search by name - N";
    char dowhat;
    cin >> dowhat;
    if (dowhat == 'T'){
        cout << "Enter number";
        unsigned long long tel;
        cin >> tel;
        find_with_tel(tel, book, n);
    }
    if (dowhat == 'N') {
        cout << "Enter name";
        string name;
        cin >> name;
        find_with_name(name, book, n);
    }
    return 0;
}