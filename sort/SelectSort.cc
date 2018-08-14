#include <iostream>

#include "utils.h"

using namespace std;

void SelectSort(IntArray &input_data, IntArray &output_data){
    output_data = input_data;

    for(ArrayIter out_iter = output_data.begin(); out_iter != output_data.end(); out_iter ++){
        ArrayIter min_iter = out_iter;
        for(ArrayIter in_iter = out_iter + 1; in_iter != output_data.end(); in_iter ++){
            if(*min_iter > *(in_iter)){
                min_iter = in_iter;
            }
        }

        if(min_iter != out_iter){
            int temp = *min_iter;
            *min_iter = *out_iter;
            *out_iter = temp;
        }
    }
}

int main(int argc, char const *argv[])
{
    IntArray input_data, output_data;
    GetRandomArray(input_data, 0, 100, 10);
    cout << "Raw input:" << endl;
    PrintArray(input_data);

    SelectSort(input_data, output_data);

    cout << "Result output:" << endl;
    PrintArray(output_data);

    return 0;
}
