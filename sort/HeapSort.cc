#include <iostream>

#include "utils.h"

using namespace std;

void BuildSort(IntArray &input_data, int index, int len){
    //置顶向下调整
    for (int i = index; i < input_data.size();)
    {
        int left_child_index = 2 * i + 1;
        int max_child_index = left_child_index;
        
        if(left_child_index >= len){
            //无子节点
            break;
        }

        if (left_child_index + 1 < len && input_data[left_child_index + 1] > input_data[left_child_index]){
            max_child_index = left_child_index + 1;
        }

        if (input_data[i] > input_data[left_child_index]){
            //接下去的不用调整了
            break;
        }else{
            //交换
            int temp = input_data[max_child_index];
            input_data[max_child_index] = input_data[i];
            input_data[i] = temp;
        }
        i = max_child_index;
    }
}

void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

void HeapSort(IntArray &input_data){
    for(int i = input_data.size()/2 - 1; i >=0; i-- ){
        BuildSort(input_data, i, input_data.size());
    }

    for(int i = input_data.size(); i > 0; i--){
    
        swap(input_data[0], input_data[i - 1]);
        BuildSort(input_data, 0, i-1);      //是i-1而不是i
    }
}

int main(int argc, char const *argv[])
{
    IntArray input_data, output_data;
    GetRandomArray(input_data, 0, 100, 100);
    cout << "Raw input:" << endl;
    
    PrintArray(input_data);

    HeapSort(input_data);

    cout << "Result output:" << endl;
    PrintArray(input_data);

    return 0;

    return 0;
}
