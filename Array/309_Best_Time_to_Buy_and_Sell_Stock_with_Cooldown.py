import unittest


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        buy,sell = -prices[0],0
        last_buy = 0
        last_sell = 0

        for price in prices:
            last_buy = buy
            buy = max(last_buy, last_sell  - price)
            last_sell = sell
            sell = max(last_sell, last_buy + price)
        
        return sell


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1, 2, 3, 0, 2]
        self.assertEqual(self.s.maxProfit(input), 3)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
