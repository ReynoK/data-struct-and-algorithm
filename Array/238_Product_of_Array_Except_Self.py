"""求数组除自己以外的其他元素的积，不能用除法

思路：利用输出先存储累存的值，然后再遍历一遍，逐步计算另一边的值，相乘即可得

Returns:
    [type] -- [description]
"""


import unittest

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []

        output = nums[:]

        index = len(nums) - 1
        product = 1

        while index >= 0:
            output[index] = product
            product *= nums[index]
            index -= 1

        product = 1
        for index in range(len(nums)):
            output[index] = product * output[index]
            product *= nums[index]

        return output

class TestSolution(unittest.TestCase):
    def test_one(self):
        input = [1,2,3,4]
        s = Solution()
        print(s.productExceptSelf(input))

if __name__ == "__main__":
    unittest.main()
