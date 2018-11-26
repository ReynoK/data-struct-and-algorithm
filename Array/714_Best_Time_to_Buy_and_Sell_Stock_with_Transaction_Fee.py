import unittest

class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        length = len(prices)

        if len(prices) < 2:
            return 0

        last_own = -prices[0]
        last_no_own = 0

        for i in range(1, length):
            own = max(last_own, last_no_own - prices[i])
            last_no_own = max(last_no_own, last_own + prices[i] - fee)
            last_own = own
        
        return last_no_own

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1, 3, 2, 8, 4, 9]
        self.assertEqual(self.s.maxProfit(input, 2), 8)

    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
            

            
        
