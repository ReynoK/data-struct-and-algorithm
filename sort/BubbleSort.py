import utils 

def bubble_sort(nums):
    sort_flag = True

    for i in range(len(nums) - 1):
        sort_flag = False
        for j in range(len(nums)-1, i, -1):
            if nums[j] < nums[j-1]:
                sort_flag = True
                nums[j],nums[j-1] = nums[j-1],nums[j]

        if not sort_flag:
            break
def main():
    nums = utils.get_random(0,100,10)
    print("Raw input:")
    utils.print_nums(nums)
    bubble_sort(nums)
    print("Result output:")
    utils.print_nums(nums)

if __name__ == "__main__":
    main()
