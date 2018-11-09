import time

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []

        start = 0

        while start < len(nums):
            if nums[start] == start + 1 :
                start += 1
            else:
                if nums[start] == nums[nums[start]-1]:
                    start += 1
                else:
                    temp = nums[start]
                    nums[start] = nums[temp-1]
                    nums[temp-1] = temp
                    

        for index,num in enumerate(nums):
            if num != index + 1:
                result.append(index+1)

        return result

s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

                    
