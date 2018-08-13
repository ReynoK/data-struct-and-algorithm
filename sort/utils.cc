#include "utils.h"

int GetRandom(int min, int max)
{
    srand(clock());
    int interval = max - min;
    int random = rand() % interval;

    return random + min;
}   

 