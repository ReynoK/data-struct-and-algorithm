"""寻找子数组的和，使得和大于等于指定数字的子数组长度最小

思路：两指针法，指向前后，当满足条件后，左指针往前移动，继续寻找

Returns:
    [type] -- [description]
"""


import unittest

class Solution:
    def minSubArrayLen2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        min_len = len(nums) + 1

        p = q = 0
        sum = 0

        while q < len(nums):
            sum += nums[q]

            if sum >= s:
                minlen = min(min_len, q - p + 1)
                sum = sum - nums[p] - nums[q]
                p += 1
                if min_len == 1:
                    return min_len
            else:
                q += 1

        if  min_len == len(nums) + 1:
            return 0

        return min_len

    def minSubArrayLen(self, s, nums):

        if len(nums) == 0:
            return 0

        sum_ = [0]

        for index in range(len(nums)):
            sum_.append(sum_[-1] + nums[index])

        p = q = 0
        min_len = len(nums) + 1
        
        while q < len(sum_):
            if sum_[q] - sum_[p] >= s:
                min_len = min(min_len, q - p)
                p += 1

                if min_len == 1:
                    return min_len
            else:
                q += 1
        if min_len == len(nums) + 1:
            return 0

        return min_len



class TestSolution(unittest.TestCase):
    def test_one(self):
        input = [2, 3, 1, 2, 4, 3]
        s = Solution()
        print(s.minSubArrayLen(7, input))


if __name__ == "__main__":
    unittest.main()    