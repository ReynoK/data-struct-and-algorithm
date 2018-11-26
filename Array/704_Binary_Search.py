import unittest

class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1

        l = 0
        h = len(nums) - 1

        while l < h:
            m = l + (h-l)//2
            if nums[m] <= target:
                l = m + 1
            elif nums[m] >= target:
                h = m
        
        pos = -1 
        if nums[l] > target:
            pos = l

        return pos

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [-1, 0, 3, 3, 5, 9, 12]
        self.assertEqual(self.s.search(input, 3), 4)
    
    def test_two(self):
        input = [-1, 0, 3, 3, 5, 9, 12]
        self.assertEqual(self.s.search(input, 2), 2)

    def test_three(self):
        input = [0]
        self.assertEqual(self.s.search(input, 0), -1)

if __name__ == "__main__":
    unittest.main()
