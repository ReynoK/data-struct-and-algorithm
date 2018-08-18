import utils
import time

def _partitions(nums, low, high):
    key = nums[low]

    while low < high:
        while low < high and nums[high] >= key:
            high -= 1

        if low < high:
            nums[low] = nums[high]

        while low < high and nums[low] <= key:
            low += 1

        if low < high:
            nums[high] = nums[low]

    nums[low] = key
    return low

def _quick_sort(nums, low, high):
    if low >= high:    #条件为大于或等于
        return 
    partition_index = _partitions(nums, low, high)
    _quick_sort(nums, low, partition_index)
    _quick_sort(nums, partition_index+1, high)

def quick_sort(nums):
    _quick_sort(nums, 0, len(nums) - 1 )

def main():
    nums = utils.get_random(0,100,10)
    print("Raw input:")
    utils.print_nums(nums)
    quick_sort(nums)
    print("Result output:")
    utils.print_nums(nums)

if __name__ == "__main__":
    main()