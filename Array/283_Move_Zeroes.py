"""将数组中的非0元素往前移

思路：
1. 我想复杂，用了两只针
2. 简单的方法，就是把非0元素往前移动，前面的后面覆盖前面

Returns:
    [type] -- [description]
"""


import unittest

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        l = r = 0

        while r < len(nums):
            while l < len(nums) and nums[l]!=0:
                l += 1
            while r <= l:
                r += 1

            while r < len(nums) and nums[r] == 0:
                r += 1
            if r < len(nums):
                nums[l],nums[r] = nums[r],nums[l]




class TestList(unittest.TestCase):
    def test_one(self):
        nums = [0,1,0,3,12]
        s = Solution()
        s.moveZeroes(nums)
        print(nums)


if __name__ == '__main__':
    unittest.main()