#include <iostream>

using namespace std;

//Функция, позволяющая выводить систему
void show(int** a, int n, int m) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << a[i][j] << ' ';
        }
        cout << endl;
    }
    cout << endl;
}

//Функция, проверяющая возможно ли движение дислокации
bool movable(int** a, int i, int j, int n, int m) {
    //Проверка соседства с краем
    if (i == 0 || j == 0 || i ==  (n - 1) || j == (m - 1)) {
        return false;
    } else {
        //Проверка соседства с частицами
        if (a[i][j + 1] == 1 ||
            a[i][j - 1] == 1 ||
            a[i + 1][j] == 1 ||
            a[i - 1][j] == 1) {
            return false;
        } else {
            return true;
        }
    }
}

bool same(int** a, int** b, int n, int m){
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] != b[i][j]) {return false;}
        }
    }
    return true;
}

//Функция, осуществляющая "шаги" в системе
void steps(int** a, int n, int m) {
    int step = 0;
    int** b = new int*[n];
    for (int i = 0; i < n; i++) {
        b[i] = new int[m];
        for (int j = 0; j < m; j++) {
            b[i][j] = 0;
        }
    }
    while (true) {
        step++;
        //Создание виртуальной системы. Она необходима, чтобы учесть "узкие моменты"
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                b[i][j] = 0;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                //Перенос в виртуальную систему неподвижных дислокаций
                if (a[i][j] == 1 && !movable(a, i, j, n, m)) {
                    b[i][j] = 1;
                }
                //Перенос движущихся: если при движении дислокации в заданном направлении уже есть дислокация,
                //то перемещения не происходит
                if (a[i][j] == 1 && movable(a, i, j, n, m)) {
                    int direction = rand() % 4;
                    if (direction == 0) {
                        if (b[i][j + 1] == 0) {b[i][j + 1] = 1;}
                        else {b[i][j] = 1;}
                    }
                    if (direction == 1) {
                        if (b[i][j - 1] == 0) {b[i][j - 1] = 1;}
                        else {b[i][j] = 1;}
                    }
                    if (direction == 2) {
                        if (b[i + 1][j] == 0) {b[i + 1][j] = 1;}
                        else {b[i][j] = 1;}
                    }
                    if (direction == 3) {
                        if (b[i - 1][j] == 0) {b[i - 1][j] = 1;}
                        else {b[i][j] = 1;}
                    }
                }
            }
        }
        if (same(a, b, n, m)) {
            cout << step << endl;
            break;
        }
        //Замена системы ее виртуальной
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                a[i][j] = b[i][j];
            }
        }
        //show(a, n, m);
    }
}
bool movable_one_size(int** a, int j, int m) {
    //Проверка соседства с краем
    if ( j == 0 || j == (m - 1)) {
        return false;
    } else {
        //Проверка соседства с частицами
        if (a[0][j + 1] == 1 ||
            a[0][j - 1] == 1
                ) {
            return false;
        } else {
            return true;
        }
    }
}
void steps_one_size(int** a, int m) {
    int step = 0;
    int** b = new int*[1];

    b[0] = new int[m];
    for (int j = 0; j < m; j++) {
        b[0][j] = 0;

    }
    while (true) {
        step++;
        //Создание виртуальной системы. Она необходима, чтобы учесть "узкие моменты"

        for (int j = 0; j < m; j++) {
            b[0][j] = 0;}


        for (int j = 0; j < m; j++) {
            //Перенос в виртуальную систему неподвижных дислокаций
            if (a[0][j] == 1 && !movable_one_size(a, j, m)) {
                b[0][j] = 1;
            }
            //Перенос движущихся: если при движении дислокации в заданном направлении уже есть дислокация,
            //то перемещения не происходит

            if (a[0][j] == 1 && movable_one_size(a, j, m)) {
                int direction = rand() % 2;
                if (direction == 0) {
                    if (b[0][j + 1] == 0) {b[0][j + 1] = 1;}
                    else {b[0][j] = 1;}
                }
                if (direction == 1) {
                    if (b[0][j - 1] == 0) {b[0][j - 1] = 1;}
                    else {b[0][j] = 1;}
                }
            }
        }

        if (same(a, b, 1, m)) {
            cout << step << endl;
            break;
        }
        //Замена системы ее виртуальной

        for (int j = 0; j < m; j++) {
            a[0][j] = b[0][j];
        }

    }
}


int main() {
    cout << "t - test, f - 1 problem, s - 2 problem, F/S - 3 problem";
    char type;
    cin >> type;
    if (type == 't') {
        int n = 0, m = 0;
        cin >> n >> m;
        int** a = new int*[n];
        for (int i = 0; i < n; i++) {
            a[i] = new int[m]{};
        }

        double k = 0, l = 0;
        cin >> k;
        //Генерация системы
        //while(l/(n*m - l) <= k) {
        while(l <= k){
            int i = 0, j = 0;
            i = rand() % n;
            j = rand() % m;
            if (a[i][j] == 0) {
                a[i][j] = 1;
                l++;
//cout << l/(n*m) << endl;
            }
        }
        steps(a, n, m);
        //steps_one_size(a, m);
        show(a, 1, m);
    }
    if (type == 'f'){
        for (int length = 10; length <= 1000; length += 20){

            int **a = new int *[length];
            for (int i = 0; i < length; i++) {
                a[i] = new int[length]{};
            }

            int i = 0, j = 0;
            i = rand() % length;
            j = rand() % length;
            a[i][j] = 1;
            steps(a, length, length);
        }
    }
    if (type == 's'){
        for (int length = 10; length <= 1000; length += 100){
            for (double k = 0.1; k<=1; k+=0.1){
                int **a = new int *[length];
                for (int i = 0; i < length; i++) {
                    a[i] = new int[length]{};
                }
                double l = 0;
                while (l/(length*length - l) <= k) {
                    int i = 0, j = 0;
                    i = rand() % length;
                    j = rand() % length;
                    if (a[i][j] == 0) {
                        a[i][j] = 1;
                        l++;
                    }
                }
                steps(a, length, length);}
        }
    }
    if (type == 'F'){
        for (int length = 10; length <= 700; length += 10){

            int **a = new int *[1];
            a[0] = new int[length]{};


            int i = 0, j = 0;
            i = 0;
            j = rand() % length;
            a[i][j] = 1;
            steps_one_size(a, length);
        }
    }
    if (type == 'S'){
        for (int length = 10; length <= 1010; length += 100){
            for (double k = 0.1; k<=1; k+=0.1){

                int **a = new int *[1];
                a[0] = new int[length]{};

                double l = 0;
                while (l/(length - l) <= k) {
                    int i = 0, j = 0;
                    i = 0;
                    j = rand() % length;
                    if (a[i][j] == 0) {
                        a[i][j] = 1;
                        l++;
                    }
                }
                steps_one_size(a, length);}
        }
    }

    return 0;
}

