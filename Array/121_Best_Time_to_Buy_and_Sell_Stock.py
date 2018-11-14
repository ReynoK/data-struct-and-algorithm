import unittest


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) == 0:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price > min_price:
                max_profit = max(max_profit, price - min_price)
            else:
                min_price = min(min_price, price)

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
