/***
 * Требуется:
 * 1. Реализовать алгоритм медленной сортировки (один из: сортировка выбором, вставками, пузырьком) +
 * 2. Реализовать алгоритм быстрой сортировки (сортировка Хоара или сортировка слиянием) +
 * 3. Реализовать алгоритмы поиска элемента в отсортированном массиве (тривиальный алгоритм, бинарный поиск) +
* Вопросы к заданию:
 * 1. Определить зависимость времени работы медленной сортировки (сортировки выбором) от числа элементов массива +
 * 2. Определить зависимость времени работы быстрой сортировки (сортировка Хоара/сортировка слиянием)  от числа элементов массива +
 * 3. Определить количество элементов массива при котором медленная сортировка работает быстрее быстрой. +
 * 4. Определить зависимость времени работы тривиального поиска от количества элементов массива и количества запросов поиска +
 * 5. Определить зависимость времени работы бинарного поиска от количества элементов массива и количества запросов поиска +
 * 6. Обменяться кодами быстрой сортировки с одногрупниками, провести исследование времени работы альтернативного алгоритма.
 * 7. Определить диапазоны значений параметра N, для которых тот или иной алгоритм сортировки применим
 * 7. Ответ: медленная - 20 (потом лучше быстрая), быстрая - 101000
 * 8. Определите максимальное значение параметра MAX_N (с точностью до десятков тысяч) при котором программа может работать
 * 8. Ответ: 101000
*/

#include <iostream>
#include <utility>
#include "extension.hpp"

unsigned long long const MAX_N = 100000; //Максимальное количество элементов в массиве

//******************************Поиск элемента в массиве**********************************

unsigned long tr_search(long data[], unsigned long size,  unsigned long key){
    for (unsigned long i = 0; i < size; i++){
        if (data[i] == key){
            return i;
        }
    }
    return -1;
}

unsigned long bin_search(long data[], unsigned long size,  unsigned long key) {
    unsigned long l = 0, r = size;

    while (l < r) {
        auto mid = (l + r) / 2;
        if (key < data[mid])
            r = mid;
        else if (data[mid] < key)
            l = mid + 1;
        else
            return mid;
    }
    return -1;
}



//***********************Сортировка пузырьком********************************************

void bubble_sort(long data[], unsigned long size){
    for(unsigned long i = 0; i<size; i++){
        bool flag = true;
        for(unsigned long j = 0; j < (size - (i+1)); j++){
            if (data[j] > data[j+1]){
                std::swap (data[j], data[j+1]);
                flag = false;
            }
        }if (flag == true){
            return;
        }
    }

}


//**********************************Сортировка Хоара*************************************

unsigned long partition(long data[], unsigned long l, unsigned long r, long mid) {
    while (true) {
        while (data[l] < mid) {
            l = l+1;}
        while (data[r] > mid) {
            r = r-1;}
        if (r <= l){
            return r;
        }
        std::swap(data[l++], data[r--]);
    }
}
void hoare_sort(long data[], unsigned long l, unsigned long r){
    if (l>=r){
        return;
    }
    unsigned long split = partition(data, l, r, data[(l+r)/2]);
    hoare_sort(data, l, split);
    hoare_sort(data, split+1, r);
}
//***************************************************************************************

void search_test_function(long A[MAX_N], unsigned long N, unsigned long requests_counts){
  Utils util;
  long *requests =new long[requests_counts];
  util.generate_data(requests, requests, requests_counts);

  Timer t; t.start();
  unsigned long misses = 0;
  for (auto i = 0ul; i < requests_counts; ++i){
    unsigned long index = 0;
    index = bin_search(A, N, requests[i]);
    //index = tr_search(A, N, requests[i]);
    if (index >= N){
      ++misses;
    }
    if (index < N && A[index] != requests[i]){
      std::cout << "Fail to search " << requests[i] << ". A[index] == " << A[index] << std::endl;
      return;
    }
  }
  t.stop();

  std::cout << "Processed " << requests_counts << " requests for array size " << N << ". Missed "<< misses
            << " requests. Elapsed time: "
            << t.elapsed() << " microseconds." << std::endl;

  delete[] requests;
}

int main() {
  Utils util;

  long slow_data[MAX_N], rapid_data[MAX_N];

  unsigned long const N = 1000; //Варьируемый параметр. Можно смело изменять для получения зависимости времени от N. N <= MAX_N

  //Генерация N произвольных числе из отрезка [-1000, 1000] в массивы slow_data и rapid_data. slow_data[i] == rapid_data[i]
  util.generate_data(slow_data, rapid_data, N);

  //*****************************Тестирование медленной сортировки******************************************************
  {
    Timer t;
    t.start();

    //Разместите вызов функции медленной сортировки для массива slow_data здесь

    bubble_sort(slow_data, N);

    t.stop();

    if (!util.check_order(slow_data, N)) {
      std::cout << "Sort order is wrong(S). Check the sort function." << std::endl;
    } else {
      std::cout << "Performed slow sort of " << N << " elements. Elapsed time: " << t.elapsed() << " microseconds.\n" ;
    }
    std::cout << "First min(" << N << ", 10) elements:\n";
    for (auto i = 0; i < std::min(N, 10ul); ++i)
      std::cout << slow_data[i] << " ";
    std::cout << std::endl;
  }
  //********************************************************************************************************************

  //*****************************Тестирование быстрой сортировки********************************************************
  {
    Timer t;
    t.start();

    //Разместите вызов функции быстрой сортировки для массива rapid_data здесь
    auto r = N-1;
    hoare_sort(rapid_data, 0, r);


    t.stop();

    if (!util.check_order(rapid_data, N)) {
      std::cout << "Sort order is wrong(F). Check the sort function." << std::endl;
    } else {
      std::cout << "Performed rapid sort of " << N << " elements. Elapsed time: " << t.elapsed() << " microseconds.\n";
    }

    std::cout << "First min(" << N << ", 10) elements:\n";
    for (auto i = 0; i < std::min(N, 10ul); ++i)
      std::cout << rapid_data[i] << " ";
    std::cout << std::endl;
  }
  //********************************************************************************************************************

  //*****************************Тестирование поиска элемента в массиве*************************************************
  unsigned long request_count = 1000; //Количество запросов поиска. Можно варьировать в неограниченных (в разумной степени) пределах
  search_test_function(slow_data, N, request_count);
  //********************************************************************************************************************
  return 0;
}
