import unittest


class Solution:
    def maxProfit(self, k, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        if k >= len(prices)/2:
            maxPro = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    maxPro += prices[i] - prices[i-1]
            return maxPro

        buy = [[0]*(len(prices) + 1) for i in range(2)]
        sell = [[0]*(len(prices) + 1) for i in range(2)]

        for k in range(1, k+1):
            k %= 2  
            buy[k][0] = buy[k][1] = -prices[0]
            for i in range(2, len(prices)+1):
                buy[k][i] = max(buy[k][i-1], sell[k-1][i-1]-prices[i-1])
                sell[k][i] = max(sell[k][i-1], buy[k][i-1] + prices[i-1])
        return max(sell[0][-1], sell[-1][-1])

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    # def test_one(self):
    #     input = [2, 4, 1]
    #     self.assertEqual(self.s.maxProfit(2,input), 2)
    
    # def test_two(self):
    #     input = [3, 2, 6, 5, 0, 3]
    #     self.assertEqual(self.s.maxProfit(2, input), 7)

    def test_three(self):
        input = [1, 2]
        self.assertEqual(self.s.maxProfit(1, input), 1)
if __name__ == "__main__":
    unittest.main()
