import utils

def insert_sort(nums):
    temp = []
    for num in nums:
        if len(temp) == 0 or num > temp[-1]:
            temp.append(num)
        else:
            temp.append(num)
            i = len(temp) - 2
            while temp[i] > num and i > -1:
                temp[i+1] = temp[i]
                i -= 1
            temp[i+1] = num

    for i in range(len(nums)):
        nums[i] = temp[i]

def main():
    nums = utils.get_random(0,100,10)
    print("Raw input:")
    nums= [2,0,2,1,1,0]
    utils.print_nums(nums)
    insert_sort(nums)
    print("Result output:")
    utils.print_nums(nums)

if __name__ == "__main__":
    main()