#include <iostream>

#include "utils.h"

using namespace std;

void BubbleSort(IntArray &input_data, IntArray &output_data)
{
    output_data = input_data;
    bool sort_flag = true;      

    for (ArrayIter out_iter = output_data.begin(); out_iter != output_data.end() && sort_flag; out_iter++)
    {
        sort_flag = false;
        for (ArrayIter in_iter = output_data.end() - 1; in_iter > out_iter; in_iter--){
            if(*in_iter < *(in_iter - 1)){
                sort_flag = true;           //如果没有走到这一步，那么序列现在已经有序，无需在进行下去
                int temp = *in_iter;
                *in_iter = *(in_iter - 1);
                *(in_iter - 1) = temp;
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    IntArray input_data, output_data;
    GetRandomArray(input_data, 0, 100, 100);
    cout << "Raw input:" << endl;;
    PrintArray(input_data);

    BubbleSort(input_data, output_data);

    cout << "Result output:"<<endl;
    PrintArray(output_data);

    return 0;
}
