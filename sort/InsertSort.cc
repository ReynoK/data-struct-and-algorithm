#include <iostream>
#include <limits>

#include "utils.h"

using namespace std;

void InsertSort(IntArray &data)
{
    IntArray temp;
    for (ArrayIter input_iter = data.begin(); input_iter != data.end(); input_iter++)
    {
        if (temp.empty() || *input_iter > temp.back())
        {
            temp.push_back(*input_iter);
        }
        else
        {
            temp.push_back(INT_MIN);
            ArrayIter output_iter;
            // 终止条件比较复杂
            for (output_iter = temp.end() - 1; *(output_iter - 1) > *input_iter && output_iter > temp.begin(); output_iter--)
            {
                *(output_iter) = *(output_iter-1);
            }

            *output_iter = *input_iter;
        }
    }
    data = temp;
}

int main(int argc, char const *argv[])
{
    IntArray data;
    GetRandomArray(data, 0, 100, 10);
    cout << "Raw input:" << endl;
    PrintArray(data);

    InsertSort(data);

    cout << "Result output:" << endl;
    PrintArray(data);

    return 0;
}