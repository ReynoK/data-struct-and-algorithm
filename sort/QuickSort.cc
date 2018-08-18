#include <iostream>

#include "utils.h"
using namespace std;

void Partition(IntArray &input, int low, int high, int &partition_index)
{
    int key = input[low];

    while (low < high)
    {
        //找到右侧小于key的值
        while (low < high && input[high] > key)
        {
            high--;
        }
        //移动到左边
        if (low < high)
        {
            int temp = input[low];
            input[low] = input[high];
            input[high] = temp;
        }
        //寻找左边大于key 的值
        while (low < high && input[low] <= key)
        {
            low++;
        }
        //移动到右边
        if (low < high)
        {
            int temp = input[low];
            input[low] = input[high];
            input[high] = temp;
        }
        //low~hight又是跟初始状态一样，再继续寻找
    }

    partition_index = low;
}

void QSort(IntArray &input, int low, int high)
{
    if (low >= high)
    {
        return;
    }

    int partition_index = -1;
    /*
    原理：元素在排序中所在的位置，之前的元素都比该元素小，之后的元素都比该元素大
    因此快排的原理就是寻找位置，使得之前的元素比该值小，之后的元素比该值大
    */
    Partition(input, low, high, partition_index);
    QSort(input, low, partition_index - 1);
    QSort(input, partition_index + 1, high);
}

void QuickSort(IntArray &input_data)
{
    int low = 0;
    int high = input_data.size() - 1;

    QSort(input_data, low, high);
}

int main(int argc, char const *argv[])
{
    IntArray input_data, output_data;
    GetRandomArray(input_data, 0, 100, 10);
    cout << "Raw input:" << endl;

    PrintArray(input_data);

    QuickSort(input_data);

    cout << "Result output:" << endl;
    PrintArray(input_data);

    return 0;

    return 0;
}