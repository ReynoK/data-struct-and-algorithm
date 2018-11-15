import unittest


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_profit = nums[0]
        profit = nums[0]

        for num in nums[1:]:
            if profit < 0:
                profit = 0

            profit += num
            max_profit = max(max_profit, profit)

        return max_profit


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(self.s.maxSubArray(input), 6)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
