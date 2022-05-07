#include<iostream>

using namespace std;

struct Node
{
    Node* next = nullptr;
    double dvalue;
};

struct Stack{
    Node* first = nullptr;
    Node* last = nullptr;
};

bool isEmpty(Stack stack){
    return stack.first == nullptr;
}

void push(Stack *stack, double dvalue){
    auto node = new Node;
    node->dvalue = dvalue;
    node->next = stack->first;
    stack->first=node;
}

void pop(Stack *stack){
    if (isEmpty(*stack)){
        return;
    }
    if (stack->first->next == nullptr){
        stack->first = nullptr;
        return;
    }
    auto node = stack->first->next;
    stack->first=node;
    return;
}

void stack_top(Stack stack) {
    if (isEmpty(stack)) {
        cout << "Stack is empty" << endl;
        return;
    } else {
        cout << stack.first->dvalue << endl;
    }
}

int main(){
    Stack test;
    stack_top(test);
    push(&test, 12.3);
    push(&test, 12.4);
    push(&test, 13.8);
    stack_top(test);
    pop(&test);
    pop(&test);
    stack_top(test);
    pop(&test);
    stack_top(test);
}
