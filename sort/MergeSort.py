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

def _merge_sort(nums, left, right):
    if left == right:
        return

    mid = int((left+right) / 2)

    _merge_sort(nums, left, mid)
    _merge_sort(nums, mid+1, right)
    _merge(nums, left, mid, right)

def merge_sort(nums):
    _merge_sort(nums, 0, len(nums)-1)

def main():
    nums = utils.get_random(0,100,10)
    print("Raw input:")
    utils.print_nums(nums)
    merge_sort(nums)
    print("Result output:")
    utils.print_nums(nums)

if __name__ == "__main__":
    main()

    
