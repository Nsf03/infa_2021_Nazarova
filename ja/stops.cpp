#include <iostream>
#include <algorithm>
using namespace std;

//Выбираем, до какой остановки смодем проехать сейчас и вписываем ее в массив нужных нам, потом повторяем уже без нее
struct Answer{
    int* nums;
    int num;
};
int take_next(int start, int N, int mileage, int* coords){ //start номер заправки
    if (coords[start+1] - coords[start] > mileage){
        return -10;
    }
    while (coords[start+1] - coords[start] <= mileage & start!= N-1){
        mileage -= coords[start+1] - coords[start];
        start +=1;
    }
    return start; //новая начальная точка
}

Answer take_all(int N, int mileage, int* coords){
    int* right_num = new int [N];
    Answer answer{};
    int start = 0;
    unsigned int i = 0;
    while (start != N-1){
        start = take_next(start, N, mileage, coords);
        if (start == -10){
            answer.num = start;
            return answer; //вдруг невозможно доехать
        }
        right_num[i] = start;
        i++;
    }
    right_num[i] = N-1;
    answer.num = i;
    answer.nums = new int[i];
    for (int j = 0; j < i; ++j) {
        answer.nums[j] = right_num[j];
    }
    return answer;
}


int main() {
    int N;
    cout << "Enter N";
    cin >> N;
    int* coords = new int[N];
    cout << "Enter mileage";
    int mileage;
    cin >> mileage;
    cout << "Enter coords (with 0!)";
    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a;
        coords[i] = a;
    }
    sort(coords, coords+N);
    auto answer = take_all(N, mileage, coords);
    if (answer.num == -10){
        cout << "NOT POSSIBLE";
        return 0;
    }
    for (int i = 0; i < answer.num; ++i) {
        cout << coords[answer.nums[i]] << "   ";
    }
    return 0;
}
