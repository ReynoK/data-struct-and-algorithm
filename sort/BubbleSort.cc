#include <iostream>

#include "utils.h"

using namespace std;

void BubbleSort(IntArray &data)
{
    bool sort_flag = true;

    for (ArrayIter out_iter = data.begin(); out_iter != data.end() && sort_flag; out_iter++)
    {
        sort_flag = false;
        for (ArrayIter in_iter = data.end() - 1; in_iter > out_iter; in_iter--)
        {
            if(*in_iter < *(in_iter - 1)){
                sort_flag = true;           //优化，如果没有走到这一步，那么序列现在已经有序，无需在进行下去
                swap(in_iter, in_iter - 1);
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    IntArray data;
    GetRandomArray(data, 0, 100, 10);
    cout << "Raw input:" << endl;;
    PrintArray(data);

    BubbleSort(data);

    cout << "Result output:"<<endl;
    PrintArray(data);

    return 0;
}
