#include <iostream>

#include "utils.h"

using namespace std;

void BuildSort(IntArray &data, int index, int len)
{
    //置顶向下调整
    for (int i = index; i < data.size();)
    {
        int left_child_index = 2 * i + 1;
        int max_child_index = left_child_index;

        if (left_child_index >= len)
        {
            //无子节点
            break;
        }

        if (left_child_index + 1 < len && data[left_child_index + 1] > data[left_child_index])
        {
            max_child_index = left_child_index + 1;
        }

        if (data[i] > data[left_child_index])
        {
            //接下去的不用调整了
            break;
        }
        else
        {
            //交换
            int temp = data[max_child_index];
            data[max_child_index] = data[i];
            data[i] = temp;
        }
        i = max_child_index;
    }
}

void HeapSort(IntArray &data)
{
    for (int i = data.size() / 2 - 1; i >= 0; i--)
    {
        BuildSort(data, i, data.size());
    }

    for (int i = data.size(); i > 0; i--)
    {

        swap(data[0], data[i - 1]);
        BuildSort(data, 0, i - 1); //是i-1而不是i
    }
}

int main(int argc, char const *argv[])
{
    IntArray data;
    GetRandomArray(data, 0, 100, 100);
    cout << "Raw input:" << endl;

    PrintArray(data);

    HeapSort(data);

    cout << "Result output:" << endl;
    PrintArray(data);

    return 0;
}
