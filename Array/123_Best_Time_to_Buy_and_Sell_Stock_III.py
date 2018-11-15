import unittest
from pprint import pprint

class Solution:
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        buy = [[0]*(len(prices) + 1) for i in range(3) ]
        sell = [[0]*(len(prices) + 1) for i in range(3)]

        # buy[0][1] = buy[0][0] = -prices[0]
        buy[1][0] = buy[1][1] = -prices[0]
        buy[2][0] = buy[2][1] = -prices[0]

        for k in range(1,3):
            for i in range(2, len(prices)+1):
                buy[k][i] = max(buy[k][i-1], sell[k-1][i-1]-prices[i-1])
                sell[k][i] = max(sell[k][i-1], buy[k][i-1] + prices[i-1])
        pprint(buy)
        pprint(sell)
        return sell[-1][-1]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        buy = [[0]*(len(prices) + 1) for i in range(3)]
        sell = [[0]*(len(prices) + 1) for i in range(3)]

        # buy[0][1] = buy[0][0] = -prices[0]
        buy[1][0] = buy[1][1] = -prices[0]
        buy[2][0] = buy[2][1] = -prices[0]
        own_1,own_2,no_own_1,no_own_2 = 0,0,0,0
        own_1 = own_2 = -prices[0]

        for i in range(2, len(prices)+1):

            no_own_2 = max(no_own_2, own_2 + prices[i-1])
            own_2 = max(own_2, no_own_1 - prices[i-1])
            no_own_1 = max(no_own_1, own_1 + prices[i-1])
            own_1 = max(own_1, -prices[i-1])

        return no_own_2

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [3, 3, 5, 0, 0, 3, 1, 4]
        self.assertEqual(self.s.maxProfit(input), 6)
    
    def test_two(self):
        input = [1, 2, 3, 4, 5]
        self.assertEqual(self.s.maxProfit(input), 4)

if __name__ == "__main__":
    unittest.main()
