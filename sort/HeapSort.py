import utils

def build_heap(nums, heap_index, end):
    while heap_index <=end:

        left_index = 2 * heap_index + 1
        right_index = 2 * heap_index + 2
        max_child_index = left_index

        if left_index > end:
            return 

        if right_index <= end and nums[right_index] > nums[left_index]:
            max_child_index = right_index

        if nums[max_child_index] <= nums[heap_index]:
            return 

        nums[heap_index],nums[max_child_index] = nums[max_child_index],nums[heap_index]
        heap_index = max_child_index
        
def heap_sort(nums):
    for heap_index in range(int(len(nums)/2) - 1, -1, -1):
        build_heap(nums, heap_index, len(nums) - 1)

    for i in range(len(nums)-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        build_heap(nums, 0, i-1)

def main():
    nums = utils.get_random(0,100,10)
    print("Raw input:")
    utils.print_nums(nums)
    heap_sort(nums)
    print("Result output:")
    utils.print_nums(nums)

if __name__ == "__main__":
    main()
