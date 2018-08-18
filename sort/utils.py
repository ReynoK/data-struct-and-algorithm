import random

CONST_ROW_NUM = 10

def get_random(min, max, num):
    return [int(random.random()*(max-min)) + min for i in range(num)]

def print_nums(nums):
    for i in range(len(nums)):
        if i!=0 and i%CONST_ROW_NUM == 0:
            print()
        print("%-10d"%(nums[i]), end="")

    print()