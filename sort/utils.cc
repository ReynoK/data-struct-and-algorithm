#include "utils.h"

int GetRandom(int min, int max)
{
    srand(clock());
    int interval = max - min;
    int random = rand() % interval;

    return random + min;
}   

void GetRandomArray(IntArray &array, int min, int max, uint32_t size){
    while(size--){
        array.push_back(GetRandom(min, max));
    }
}

void PrintArray(const IntArray &array)
{
    const int ROW_NUM = 20;
    const int WIDTH = 8;
    int row_index = 0;   
    for (IntArray::const_iterator iter = array.begin(); iter != array.end(); iter++)
    {
        std::cout.setf(std::ios::left);
        std::cout.width(WIDTH);
        std::cout << *iter;
        row_index ++;
        if(row_index == ROW_NUM){
            std::cout << std::endl;
            row_index = 0;
        }   
    }
    std::cout << std::endl;
}

void swap(ArrayIter val1, ArrayIter val2){
    int temp = *val1;
    *val1 = *val2;
    *val2 = temp;
}

void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}