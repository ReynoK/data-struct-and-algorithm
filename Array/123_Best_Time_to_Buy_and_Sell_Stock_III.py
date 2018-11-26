import unittest
from pprint import pprint

class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        length = len(prices)

        own = [[0]*(length) for i in range(3)]
        no_own = [[0]*(length) for i in range(3)]

        own[1][0] = own[2][0] = -prices[0]

        for k in range(1,3):
            for j in range(1, length):
                own[k][j] = max(own[k][j-1], no_own[k-1][j-1] - prices[j])
                no_own[k][j] = max(no_own[k][j-1], own[k][j-1] + prices[j])
        return no_own[-1][-1]

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

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
