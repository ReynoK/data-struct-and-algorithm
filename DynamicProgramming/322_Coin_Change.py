import unittest

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            min_change = amount + 1
            for coin in coins:
                if coin <= i:
                    min_change = min(min_change, dp[i - coin] + 1)
            dp[i] = min_change
        return dp[amount] if dp[amount] < amount + 1 else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1, 2, 5]
        self.assertEqual(self.s.coinChange(input, 11), 3)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
