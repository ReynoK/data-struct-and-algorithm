#include <iostream>
#include <vector>

#include "utils.h"

using namespace std;

void Merge(IntArray::iterator iter, uint32_t left, uint32_t mid, uint32_t right)
{
    IntArray temp_array;
    uint32_t left_index = left, right_index = mid + 1;
    //比较
    while (left_index <= mid && right_index <= right)
    {
        if (*(iter + left_index) < *(iter + right_index))
        {
            temp_array.push_back(*(iter + left_index));
            left_index++;
        }
        else
        {
            temp_array.push_back(*(iter + right_index));
            right_index++;
        }
    }
    //将剩余的复制过去
    while (left_index <= mid)
    {
        temp_array.push_back(*(iter + (left_index++)));
    }
    //将剩余的复制过去
    while (right_index <= right)
    {
        temp_array.push_back(*(iter + (right_index++)));
    }
    //注意坐标的变化
    int begin_index = 0;
    while (begin_index + left <= right)
    {
        *(iter + left + begin_index) = temp_array[begin_index];
        begin_index++;
    }
}

void _MergeSort(IntArray::iterator iter, uint32_t left, uint32_t right)
{
    if (left == right)
    {
        return;
    }

    uint32_t mid = (right + left) / 2;

    _MergeSort(iter, left, mid); //递归归并排序
    _MergeSort(iter, mid + 1, right);
    Merge(iter, left, mid, right); //合并
    return;
}

void MergeSort(IntArray &input_data)
{
    _MergeSort(input_data.begin(), 0, input_data.size() - 1);
}

int main(int argc, char const *argv[])
{
    const uint32_t TEST_NUM_COUNT = 10;
    const int MIN_NUM = 0;
    const int MAX_NUM = 100;

    IntArray input_data;
    GetRandomArray(input_data, MIN_NUM, MAX_NUM, TEST_NUM_COUNT);
    cout << "Raw input:" << endl;
    PrintArray(input_data);

    MergeSort(input_data);

    cout << "Raw input:" << endl;
    PrintArray(input_data);

    return 0;
}
