import unittest


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1        

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = i
            sqrt = int(i**0.5)
            if sqrt*sqrt == i:
                dp[i] = 1
                continue
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.numSquares(12), 3)
    
    def test_two(self):
        self.assertEqual(self.s.numSquares(13), 2)

if __name__ == "__main__":
    unittest.main()
