"""缺少的元素

思路1：想复杂了，根据元素的值将对应坐标的值改为可标识的
思路2：利用数学公式。。。。

Returns:
    [type] -- [description]
"""


import unittest

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for num in nums:
            real_num = num
            if num < 0:
                real_num = num + length + 1
            if real_num < length:
                nums[real_num] = nums[real_num] - length - 1
        for index,num in enumerate(nums):
            if num >= 0:
                return index
        
        return length

class TestList(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_mid(self):
        arr = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        print(self.s.missingNumber(arr))

    def test_tail(self):
        arr = [2,0]
        print(self.s.missingNumber(arr))

if __name__ == "__main__":
    unittest.main()
