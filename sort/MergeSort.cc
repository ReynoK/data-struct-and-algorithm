#include <iostream>
#include <vector>

#include "utils.h"

using namespace std;

void Merge(IntArray::iterator iter_begin_1, IntArray::iterator iter_begin_2, uint32_t left, uint32_t right){
    IntArray temp_array;
    uint32_t left_index = 0, right_index=0;
}

void MergeSort(IntArray::iterator iter_begin, IntArray::iterator iter_end){

    if(iter_begin == iter_end){
        return;
    }
    
    IntArray::size_type mid = (iter_end - iter_begin)/2;

    MergeSort(iter_begin, iter_begin + mid); //递归归并排序 
    MergeSort(iter_begin+mid + 1, iter_end);

    return;
}

int main(int argc, char const *argv[])
{
    const uint32_t TEST_NUM_COUNT = 100;
    const int MIN_NUM = 0;
    const int MAX_NUM = 100;

    IntArray input_data;
    GetRandomArray(input_data, MIN_NUM, MAX_NUM, TEST_NUM_COUNT);

    cout << "Raw input:" << endl;
    PrintArray(input_data);

    return 0;
}
