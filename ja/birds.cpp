#include <iostream>
#include <algorithm>

using namespace std;

struct bird{
    int start;
    int end;
    bool done = false;
};

void take_next(int n, int N, bird* birds) {//в каком месте фоткаем; n - стартовая птица
    birds[n].done = true;
    for (int i = n+1; i < N; ++i) {
        if (!birds[i].done and birds[i].start<=birds[n].end-1){
            birds[i].done = true;
        }
    }
}

bool is_done(int N, bird* birds ){
    for (int i = 0; i < N; ++i){
        if (!birds[i].done){return false;}
    }
    return true;
}

int answer(int N, bird* birds){
    int q = 0;
    for (int i = 0; i < N; ++i) {
        if (is_done(N, birds)){return q;}
        if (!birds[i].done){
            cout << "time: " << birds[i].end - 1 << endl;
            q++;
            take_next(i, N, birds);
        }
    }
}

bool comp(bird a, bird b){
    return (a.end < b.end);
}

int main(){
    int N;
    cout << "How many birds?" << endl;
    cin >> N;
    auto birds = new bird[N];
    cout << "Enter the start and end times for each bird (USE INT!!!)" << endl;
    for (int i = 0; i < N; ++i) {
        cin >> birds[i].start;
        cin >> birds[i].end;
    }
    sort(birds, birds+N, comp);
    auto q = answer(N, birds);
    cout << q << " photos";
    return 0;
}