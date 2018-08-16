#include <iostream>
#include <unistd.h>
#include "utils.h"

using namespace std;

//合并子序列
void Merge(IntArray &input, IntArray &output, int left, int mid, int right)
{
    int left_index = left, right_index = mid + 1;
    int start_index = left;

    while (left_index <= mid && right_index <= right)
    {
        if (input[left_index] < input[right_index])
        {
            output[start_index++] = input[left_index];
            left_index++;
        }
        else
        {
            output[start_index++] = input[right_index];
            right_index++;
        }
    }
    while (left_index <= mid)
    {
        output[start_index++] = input[left_index];
        left_index++;
    }

    while (right_index <= right)
    {
        output[start_index++] = input[right_index];
        right_index++;
    }
}

void MergeSort(IntArray &input)
{
    int len = (int32_t)(input.size());      //转化为有符号整型，防止下面计算的时候负数变为正整数（len-2*k -1） 
    IntArray output(input.size(), 0);
    //k表示合并的子序列长度，大于len就无意义了，每次以2的倍数增长
    for (int k = 1; k < len; k *= 2)      
    {
        int l = 0;
        //序号0开始， 一直到要合并的第二对合并子序列，因为最后一对可能长度不够，因此终止条件为  len-1 - 2*k
        //如果恰好最后一对也是两个k序列，那么  刚刚len-1-2*k +2*k 为最后一个序号
        for (l = 0; l <= len  - 2 * k - 1; l += 2 * k)
        {
            Merge(input, output, l,  l + k - 1  , l+2*k - 1 );
        }
        //l是最后一对要合并的序列的起始序号，如果剩余的序列长度>k要合并，否则不需要合并
        if(len - l >= k)
        {
            Merge(input, output, l, l + k - 1, len - 1);
        }
        input = output;
    }
}

int main(int argc, char const *argv[])
{
    IntArray input_data, output_data;
    GetRandomArray(input_data, 0, 100, 10);
    cout << "Raw input:" << endl;

    PrintArray(input_data);

    MergeSort(input_data);

    cout << "Result output:" << endl;
    PrintArray(input_data);

    return 0;

    return 0;
}
