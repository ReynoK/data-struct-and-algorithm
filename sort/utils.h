#include<random>
#include<ctime>
#include<vector>
#include<iostream>

typedef std::vector<int> IntArray;
typedef IntArray::iterator ArrayIter;

void GetRandomArray(IntArray &array, int min, int max, uint32_t size);
int GetRandom(int min, int max);
void PrintArray(const IntArray &array);
void swap(ArrayIter val1, ArrayIter val2);
void swap(int &a, int &b);
