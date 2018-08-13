#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <limits>

#include "utils.h"

using namespace std;

/*
 * input_data: 输入数据数组
 * output_data: 结果数组
 * n : 要排序的数量
 */
void CountingSort(int *input_data, int *output_data, int n)
{
    //先标准化到以0位初始值
    //最大值最小值相反
    int min = INT_MAX; //初始位为整数最大值
    int max = INT_MIN; //初始化为整数最小值
    for (int i = 0; i < n; i++)
    {
        min = min > input_data[i] ? input_data[i] : min;
        max = max > input_data[i] ? max : input_data[i];
    }
    cout << "min:" << min << " max:" << max << endl;
    //统计空间
    int interval = max - min + 1; //要多分配一位
    int *counter = (int *)calloc(interval, sizeof(int));

    //统计每个数字出现的次数
    for (int i = 0; i < n; i++)
    {
        counter[input_data[i] - min]++;
    }

    //累加，计算每个数字在排序结构中最后一次所在的位置
    for (int i = 1; i < interval; i++)
    {
        counter[i] += counter[i - 1];
    }

    for (int i = 0; i < n; i++)
    {
        counter[input_data[i] - min]--;
        output_data[counter[input_data[i] - min]] = input_data[i];
    }

    free(counter);
}

int main(int argc, char const *argv[])
{
    const int TEST_NUM_CNT = 10;
    int *input_data = (int *)calloc(TEST_NUM_CNT, sizeof(int));
    assert(input_data != NULL);
    int *output_data = (int *)calloc(TEST_NUM_CNT, sizeof(int));
    assert(output_data != NULL);

    cout << "Raw input:";
    for (int i = 0; i < TEST_NUM_CNT; i++)
    {
        input_data[i] = GetRandom(0, 10);
        cout << input_data[i] << " ";
    }
    cout << endl;

    CountingSort(input_data, output_data, TEST_NUM_CNT);

    cout << "Result output:";
    for (int i = 0; i < TEST_NUM_CNT; i++)
    {
        cout << output_data[i] << " ";
    }
    cout << endl;
    free(input_data);
    free(output_data);
}
