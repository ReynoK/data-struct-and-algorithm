#include <iostream>
#include <limits>

#include "utils.h"

using namespace std;

void InsertSort(IntArray &input_data, IntArray &output_data)
{
    for (ArrayIter input_iter = input_data.begin(); input_iter != input_data.end(); input_iter++)
    {
        if ( output_data.empty() || *input_iter > output_data.back() )
        {
            output_data.push_back(*input_iter);
        }
        else
        {       
            output_data.push_back(INT_MIN);
            ArrayIter output_iter;
            // 终止条件比较复杂
            for (output_iter = output_data.end() - 1; *(output_iter-1) > *input_iter && output_iter > output_data.begin(); output_iter--)
            {
                *(output_iter) = *(output_iter-1);
            }

            *output_iter = *input_iter;
        }
        
    }
}

int main(int argc, char const *argv[])
{
    IntArray input_data, output_data;
    GetRandomArray(input_data, 0, 100, 10);
    cout << "Raw input:" << endl;
    PrintArray(input_data);

    InsertSort(input_data, output_data);

    cout << "Result output:" << endl;
    PrintArray(output_data);

    return 0;
}