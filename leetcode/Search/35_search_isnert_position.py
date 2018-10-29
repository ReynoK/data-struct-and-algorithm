import unittest

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
