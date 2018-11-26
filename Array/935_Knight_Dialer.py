import unittest


class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        jump = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        dp = [1] * 10
        MOD = 10**9 + 7

        for n in range(1, N):
            dp2 = [0] * 10
            for node,nexts in enumerate(jump):
                dp2[node] = sum([dp[x] for x in nexts])
                dp2[node] %= MOD 
            dp = dp2
        
        return sum(dp) % MOD




class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.knightDialer(2), 20)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
