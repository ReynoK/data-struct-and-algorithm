#include <iostream>
#include <limits>
#include <list>
#include <stdio.h>
#include <stdlib.h>
#include <vector.h>

#include "utils.h"

using namespace std;

typedef Bucket vector<int>;
typedef Buckets vector<Bucket>;

const int BUCKETS_SIZE = 10;

void BucketSort(int* input_data, int* output_data, int n){
    int min = INT_MAX;
    int max = INT_MIN;

    for(int i=0; i<n; i++){
        if(input_data[i] < min){
            min = input_data[i];
        }
        if(input_data[i] > max){
            max = input_data[i];
        }
    }
    int interval = max - min;
    assert(interval != 0);

    Buckets buckets;
    for(int i = 0; i < BUCKETS_SIZE; i++){
        buckets.push_back(Bucket);
    }

    for(int i=0; i<n; i++){
        int index = (int)(((input_data[i] - min)/(interval + 1))*interval); //桶排公式
        buckets[index].push_back(input_data[i]);
    }

    for(Buckets::size_type i = 0; i < Buckets.size(); i++){
        //每个桶再使用单独的排序
    }

    //遍历桶，输出到结果数组
    int index = 0;
    for(Buckets::iterator iter = buckets.begin(); iter!= buckets.end(); iter++){
        if(iter->size() == 0){
            continue;
        }

        for(Bucket::iterator bucket_iter = iter->begin(); bucket_iter != iter->end(); bucket_iter++){
            output_data[index] = *bucket_iter;
        }
    }
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
