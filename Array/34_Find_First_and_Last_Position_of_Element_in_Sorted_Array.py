import unittest


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        l = 0
        h = len(nums) - 1

        while l<h:
            m = (l + h) // 2
            if nums[m] == target:
                h = m
            elif nums[m] < target:
                l = m + 1
            else:
                h = m

        if nums[l] != target:
            return [-1,-1]

        low = l

        l = 0
        h = len(nums) - 1

        while l < h:
            m = (l+h)//2
            if nums[m] <= target:
                l = m + 1
            else:
                h = m
        high = h if nums[h] == target else h - 1
        return [low,high]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [5, 7, 7, 8, 8, 10]
        self.assertEqual(self.s.searchRange(input, 8), [3,4])
    
    def test_two(self):
        input = [5, 7, 7, 8, 8, 10]
        self.assertEqual(self.s.searchRange(input, 6), [-1,-1])

    def test_three(self):
        input = [1,1,1,3,4,4,5,6,7]
        self.assertEqual(self.s.searchRange(input, 4), [4,5])

    def test_four(self):
        input = [1, 1, 1, 3, 4, 4, 5, 6, 7]
        self.assertEqual(self.s.searchRange(input, 2), [-1, -1])

    def test_five(self):
        input = [1, 1, 1, 3, 4, 4, 5, 6, 7]
        self.assertEqual(self.s.searchRange(input, 3), [3, 3])

if __name__ == "__main__":
    unittest.main()
