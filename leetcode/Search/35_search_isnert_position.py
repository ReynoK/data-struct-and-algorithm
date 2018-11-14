import unittest

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
"""


# easy
# 总结：如果元素不存在于列表中，在 l 和 h 元素相互靠近时，此时m会落于l上，那么其实就是 a[l]与target的比较了。
# 如果a[l] > target，证明target应该插入在a[l]之前，即a[l]所在的位置。
# 如果a[l] < target，证明target应该在a[l]之后，那么可能是a[h]（因为下一次为l = m+1 == h，还要再判断），如果target != a[h](a[l])，那么就要看a[h](a[l])和targe的大小，即上一步的判断。

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        l = 0 
        h = len(nums) - 1

        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                return m

            if nums[m] > target:
                h = m - 1
            else:
                l = m + 1

        return l 

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_one(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 5), 2)

    def test_two(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 2), 1)

if __name__ == '__main__':
    unittest.main()
