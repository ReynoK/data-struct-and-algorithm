import unittest

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) < 2:
            return 0

        max_profit = 0 
        min_buy_price = prices[0]

        for price in prices:
            if price > min_buy_price:
                max_profit = max(max_profit, price - min_buy_price)
            else:
                min_buy_price = min(min_buy_price, price)
        
        return max_profit

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.s.maxProfit(input), 5)
    
    def test_two(self):
        input = [7, 6, 4, 3, 1]
        self.assertEqual(self.s.maxProfit(input), 0)

if __name__ == "__main__":
    unittest.main()
