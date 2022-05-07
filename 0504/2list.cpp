#include <iostream>
#include <cstring>

using namespace std;
//  1. Create
//  2. insert
//    2.1 insert_front O(1)
//    2.2 insert_after O(1)
//    2.3 insert_before O(N)
//  3. delete O(N)
//  4. find O(N)

struct list_data { //структура в узле означающее его значение и имя
    const char *name; //указатель
    double dvalue; // значение
};

struct forward_list { //сам узел
    list_data data; //тут лежит имя и значения
    forward_list *next; // а тут адрес на следующий
    forward_list *prev; //на прошлый
};

bool equal(list_data const &left, list_data const &right){ //? проверяем равенство правого и левого по значению И адресу
    return left.dvalue == right.dvalue && strcmp(left.name, right.name) == 0; //TODO: use strcmp for char*
}

void free_data(list_data &data){
    data.name = nullptr;
}

forward_list *create_node(list_data data) { //создаем узел
    auto node = new forward_list; //node это указатель на fl
    node->data = data; //этот fl.data = data
    node->next = nullptr; //fl.next = null
    node->prev = nullptr;
    return node;
}

forward_list *insert_front(forward_list *head, forward_list *node) { //указатель на голову и узел
    node->next = head; //добавляем узел в начало
    node->prev = nullptr;
    if (head != nullptr){
        head->prev = node;
    }
    return node;
}

forward_list *insert_back(forward_list *back, forward_list *node) { //указатель на конец и узел
    node->next = nullptr; //добавляем узел в конец
    node->prev = back;
    if (back != nullptr){
        back->next = node;
    }
    return node;
}

forward_list *insert_after(forward_list *after, forward_list *node) {
    if (after == nullptr) //если хотим добавить в конец
        return insert_front(after, node);

    node->next = after->next;
    node->prev = after;
    auto it = after->next;
    it->prev = node;
    after->next = node;
    return node;
}

forward_list *insert_before(forward_list *before, forward_list *node) {
    if (before == nullptr)
        return insert_back(before, node);

    node->next = before;
    node->prev = before->prev;
    auto it = before->prev;
    it->next = node;
    before->prev = node;
    return node;
}

forward_list* find_from_head(forward_list* head, list_data data){
    auto it = head;
    while (it != nullptr && !equal(it->data, data)){
        it = it->next;
    }
    return it;
}
forward_list* find_from_back(forward_list* back, list_data data){
    auto it = back;
    while (it != nullptr && !equal(it->data, data)){
        it = it->prev;
    }
    return it;
}


void print_list(forward_list const *head) {
    auto it = head;
    while (it != nullptr) {
        cout << it->data.name << " " << it->data.dvalue << endl;
        it = it->next;
    }
}

forward_list* delete_node_from_head(forward_list *head, forward_list *node){
    if (head == node){
        auto next_head = head->next;
        free_data(node->data);
        delete node;
        return next_head;
    }
    auto it = head;
    while (it != nullptr && it->next != node){
        it = it->next;
    }
    if (it == nullptr){
        cerr << "Wrong node for delete!\n";
        exit(-10);
    }
    it->next = node->next;

    free_data(node->data);
    delete node;
    return head;
}
forward_list* delete_node_from_back(forward_list *back, forward_list *node){
    if (back == node){
        auto prev_back = back->prev;
        free_data(node->data);
        delete node;
        return prev_back;
    }
    auto it = back;
    while (it != nullptr && it->prev != node){
        it = it->prev;
    }
    if (it == nullptr){
        cerr << "Wrong node for delete!\n";
        exit(-10);
    }
    it->prev = node->prev;

    free_data(node->data);
    delete node;
    return back;
}

int main() {
    forward_list *head = nullptr;

    auto node_1 = create_node({"Pi", 3.14});
    auto node_2 = create_node({"E", 2.7});

    head = insert_front(head, node_2);
    head = insert_front(head, node_1);

    auto node_3 = create_node({"g", 9.8});
    insert_after(node_1, node_3);

    auto node_4 = create_node({"hbar", 6.63e-31});
    insert_before(node_3, node_4);

    print_list(head);

    auto res = find_from_head(head, {"hbar", 6.63e-31});
    delete_node_from_head(head, res);

    cout << "-------------------\n";
    print_list(head);

    while (head != nullptr)
        head = delete_node_from_head(head, head);

    cout << "-------------------\n";
    print_list(head);
    return 0;
}
