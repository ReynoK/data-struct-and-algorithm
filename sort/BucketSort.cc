#include <iostream>
#include <limits>
#include <list>
#include <stdio.h>
#include <stdlib.h>
#include <vector>

#include "utils.h"

using namespace std;

typedef vector<int> Bucket;
typedef vector<Bucket> Buckets;

const int BUCKETS_SIZE = 10;

void BucketSort(int *input_data, int *output_data, int n)
{
    int min = INT_MAX;
    int max = INT_MIN;

    for (int i = 0; i < n; i++)
    {
        if (input_data[i] < min)
        {
            min = input_data[i];
        }
        if (input_data[i] > max)
        {
            max = input_data[i];
        }
    }
    double interval = max - min; //double型，否则会导致index计算全部变为0
    assert(interval != 0);

    Buckets buckets;
    for (int i = 0; i < BUCKETS_SIZE; i++)
    {
        buckets.push_back(Bucket());
    }

    for (int i = 0; i < n; i++)
    {
        int index = (int)(((input_data[i] - min) / (interval + 1)) * BUCKETS_SIZE); //桶排公式，坐落到桶中
        buckets[index].push_back(input_data[i]);
    }

    for (Buckets::size_type i = 0; i < buckets.size(); i++)
    {
        

        if (buckets[i].size() == 0)
        { //vector.size() 返回无符号整型
            continue;
        }
        //每个桶再使用单独的排序，选择排序
        for (int m = 0; m < buckets[i].size(); m++)
        {
            int min_index = m;
            for (int n = m + 1; n < buckets[i].size(); n++)
            {
                if (buckets[i][n] < buckets[i][min_index])          //与min_index进行比较
                {
                    min_index = n;
                }
            }
            if (min_index != m)
            {
                int temp = buckets[i][m];
                buckets[i][m] = buckets[i][min_index];
                buckets[i][min_index] = temp;
            }
        }
    }


    //遍历桶，输出到结果数组
    int index = 0;
    for (Buckets::iterator iter = buckets.begin(); iter != buckets.end(); iter++)
    {
        if (iter->size() == 0)
        {
            continue;
        }

        for (Bucket::iterator bucket_iter = iter->begin(); bucket_iter != iter->end(); bucket_iter++)
        {
            output_data[index] = *bucket_iter;
            index++; //自增下标
        }
    }
}

int main(int argc, char const *argv[])
{
    const int TEST_NUM_CNT = 100;
    int *input_data = (int *)calloc(TEST_NUM_CNT, sizeof(int));
    assert(input_data != NULL);
    int *output_data = (int *)calloc(TEST_NUM_CNT, sizeof(int));
    assert(output_data != NULL);

    cout << "Raw input:";
    for (int i = 0; i < TEST_NUM_CNT; i++)
    {

        input_data[i] = GetRandom(0, 100);
        cout << input_data[i] << " ";
    }

    cout << endl;

    BucketSort(input_data, output_data, TEST_NUM_CNT);

    cout << "Result output:";
    for (int i = 0; i < TEST_NUM_CNT; i++)
    {
        cout << output_data[i] << " ";
    }
    cout << endl;

    free(input_data);
    free(output_data);
}
