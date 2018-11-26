import unittest

"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

思路：一开始想的是 dp[i] = dp[j]*dp[i-j] 1<=j<i，但是比如 dp[2] = 1，但当作为拆分的整数是时，不应该再被拆分，直接取2即可。
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1]= 1

        for i in range(1, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i-j,dp[i-j]))

        return dp[-1]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.integerBreak(2), 1)
    
    def test_two(self):
        self.assertEqual(self.s.integerBreak(10), 36)

if __name__ == "__main__":
    unittest.main()
