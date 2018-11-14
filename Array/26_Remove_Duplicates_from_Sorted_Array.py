"""去除有序数组中的重复元素，在数组本地操作

思路：选择，插入

Returns:
    [type] -- [description]
"""


import unittest

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        p = 0
        index = 1

        while index < len(nums):
            if nums[index] != nums[p] and index != p:
                p += 1
                nums[p] = nums[index]
            
            index += 1

        return p + 1



class TestRemoveDuplicates(unittest.TestCase):
    def test_one(self):
        s = Solution()
        nums = [1,2,3,3,3,4,4,5,5,6]
        length = s.removeDuplicates(nums)
        self.assertEqual([1,2,3,4,5,6], nums[:length])

if __name__ == "__main__":
    unittest.main()
    