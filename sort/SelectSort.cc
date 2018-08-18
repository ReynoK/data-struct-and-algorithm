#include <iostream>

#include "utils.h"

using namespace std;

void SelectSort(IntArray &data)
{
    for (ArrayIter out_iter = data.begin(); out_iter != data.end(); out_iter++)
    {
        ArrayIter min_iter = out_iter;
        for (ArrayIter in_iter = out_iter + 1; in_iter != data.end(); in_iter++)
        {
            if (*min_iter > *(in_iter))
            {
                min_iter = in_iter;
            }
        }

        if (min_iter != out_iter)
        {
            swap(min_iter, out_iter);
        }
    }
}

int main(int argc, char const *argv[])
{
    IntArray data;
    GetRandomArray(data, 0, 100, 10);
    cout << "Raw input:" << endl;
    PrintArray(data);

    SelectSort(data);

    cout << "Result output:" << endl;
    PrintArray(data);

    return 0;
}
