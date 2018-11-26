import unittest

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        from collections import defaultdict
        if len(nums) == 0:
            return 0
        dp = defaultdict(lambda:0)

        dp[-nums[0]] +=  1
        dp[nums[0]] += 1

        for i in range(1, len(nums)):
            temp_dp = defaultdict(lambda:0)
            for key,value in dp.items():

                temp_dp[key-nums[i]] += (value)
                temp_dp[key+nums[i]] += (value)
            dp = temp_dp
        return dp[S]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1, 1, 1, 1, 1]
        self.assertEqual(self.s.findTargetSumWays(input,3), 5)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
