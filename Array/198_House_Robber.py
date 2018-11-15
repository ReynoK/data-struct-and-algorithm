import unittest


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return nums[0]

        dp = [0] * len(nums)
        dp[0]  = nums[0]
        dp[1] = max(nums[0:2])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.input = [1, 2, 3, 1]
        self.assertEqual(self.s.rob(self.input), 4)
    
    def test_two(self):
        self.input = [2, 7, 9, 3, 1]
        self.assertEqual(self.s.rob(self.input), 12)

if __name__ == "__main__":
    unittest.main()
