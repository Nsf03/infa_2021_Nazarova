#include <iostream>
#include <fstream>
using namespace std;
struct Item{
    string itemName;
    unsigned int subitem_count;
    string* subitems;
    unsigned int creation_cost;
};

unsigned int where (Item* book, string name, unsigned int n){
    for (unsigned i = 0; i<n; i++){
        if (book[i].itemName  == name){
            return i;
        }
    }
    return 999;
}

unsigned int find_price(Item he, Item* book, unsigned int n){
    if (he.subitem_count == 0){
        return he.creation_cost;
    } else {
        unsigned int sum = 0;
        sum += he.creation_cost;
        for (unsigned i = 0; i<he.subitem_count; i++){
            auto number = where(book, he.subitems[i], n);
            sum += find_price(book[number], book, n);

        }
        return sum;
    }
}


int main(){
    ifstream F;
    F.open("recipes.txt");
    unsigned n;
    F >> n;
    Item* book = new Item[n];
    for (unsigned i=0; i<n; i++){
        F >> book[i].itemName >> book[i].subitem_count;
        book[i].subitems = new string[book[i].subitem_count];
        for (unsigned j=0; j<book[i].subitem_count; j++){
            F >> book[i].subitems[j];
        }
        F >> book[i].creation_cost;
    }
    F.close();
    cout << "You want to find a cost of item - C" << endl;
    cout << "You have gold coins and want to find an amount of items - A" << endl;
    char a;
    cin >> a;
    cout << "Enter item's name" << endl;
    string name;
    cin >> name;
    auto k = where(book, name, n);
    auto price = find_price(book[k], book, n);
    if (a == 'C'){
        cout << price << " gold coins" << endl;
    }
    if (a == 'A'){
        cout << "How many gold coins do you have?" << endl;
        unsigned int gold;
        cin >> gold;
        auto amount = gold / price;
        cout << amount << " " << name << endl;
    }
    return 0;
}