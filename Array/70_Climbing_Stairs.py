import unittest

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.climbStairs(2),2)
    
    def test_two(self):
        self.assertEqual(self.s.climbStairs(3),3 )

if __name__ == "__main__":
    unittest.main()
