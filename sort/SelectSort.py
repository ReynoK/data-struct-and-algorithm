import utils

def select_sort(nums):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j

        if min_index != i:
            nums[min_index], nums[i] = nums[i], nums[min_index]

def main():
    nums = utils.get_random(0,100,10)
    print("Raw input:")
    utils.print_nums(nums)
    select_sort(nums)
    print("Result output:")
    utils.print_nums(nums)

if __name__ == "__main__":
    main()