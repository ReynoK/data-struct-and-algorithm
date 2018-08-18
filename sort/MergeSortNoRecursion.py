import utils

def _merge(nums, left, mid, right):
    temp = []
    left_index = left
    right_index = mid+1

    while left_index <= mid and right_index <= right:
        if nums[left_index] <= nums[right_index]:
            temp.append(nums[left_index])
            left_index += 1
        else:
            temp.append(nums[right_index])
            right_index += 1

    while left_index <= mid:
        temp.append(nums[left_index])
        left_index += 1

    while right_index <= right:
        temp.append(nums[right_index])
        right_index += 1

    for index,num in enumerate(temp):
        nums[left + index] = num

def merge_sort(nums):
    k = 1
    while k < len(nums):
        
        start = 0

        while start <= len(nums) - 2*k :
            _merge(nums, start, start + k - 1, start + 2*k -1)
            start += 2*k

        if len(nums) > start + k:
            _merge(nums, start, start + k -1, len(nums) - 1)

        k *= 2

def main():
    nums = utils.get_random(0,100,10)
    nums = [0,0,1,1,2,2]
    print("Raw input:")
    utils.print_nums(nums)
    merge_sort(nums)
    print("Result output:")
    utils.print_nums(nums)

if __name__ == "__main__":
    main()