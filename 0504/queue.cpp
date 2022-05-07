#include<iostream>

using namespace std;

struct Node
{
    double dvalue;
    Node* next = nullptr;
};

struct Queue
{
    Node* first = nullptr;
    Node* last = nullptr;
};


bool isEmpty(Queue sll){
    return sll.first == nullptr;
}

void push(Queue *q, double dval){
    auto node = new Node;
    node->dvalue = dval;
    if (isEmpty(*q)) {
        q->first = node;
        q->last = node;
        return;
    }
    (q->last)->next = node;
    q->last = node;
}

void pop(Queue *q){
    if (isEmpty(*q)){
        return;
    }
    if (q->first->next == nullptr){
        q->first = nullptr;
        return;
    }
    auto node = q->first->next;
    q->first=node;
    return;
}

void top(Queue q) {
    if (isEmpty(q)) {
        cout << "Queue is empty" << endl;
        return;
    }
    cout << q.first->dvalue << endl;

}

int main(){
    Queue q;
    top(q);
    for (double i=0;i<4;i=i+0.123){
        push(&q, i);
    }
    top(q);
    cout << "-----" << endl;
    while (not isEmpty(q)){
        top(q);
        pop(&q);
    }
    cout << "-----" << endl;
    top(q);
    return 0;
}