"""移动有序数组，使得数组中每个数组只出现至多2次

思路：两个指针，一个表示当前插入的位置，另一表示当前移动到的位置，该指针会将符合条件的数插入到之前的指针位置
Returns:
    [type] -- [description]
"""


import unittest

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        p = q = 0

        while q < len(nums):
            if q < 2:
                p += 1
                q += 1
                continue
            if nums[q] == nums[p-1] and nums[p-2] == nums[q]:
                q += 1
            else:
                nums[p] = nums[q]
                q += 1
                p += 1

        return p


class TestSolution(unittest.TestCase):
    def test_one(self):
        input = [1,1,1,2,2,2,3]
        s = Solution()
        length = s.removeDuplicates(input)
        print(input[:length])

    def test_two(self):
        input = [1, 1, 2, 2, 3]
        s = Solution()
        length = s.removeDuplicates(input)
        print(input[:length])

if __name__ == "__main__":
    unittest.main()