import unittest

class Solution:
    def maxProfit(self, k, prices):
        if len(prices) < 2:
            return 0
        
        length = len(prices)

        if k >= length//2:
            own = [0] * length
            no_own = [0] * length
            own[0] = -prices[0]

            for i in range(1, length):
                own[i] = max(own[i-1], no_own[i-1] - prices[i])
                no_own[i] = max(no_own[i-1], own[i] + prices[i])

            return no_own[-1]

        own = [[0]*(length) for i in range(2)]
        no_own = [[0]*(length) for i in range(2)]

        own[0][0] = own[1][0] = -prices[0]

        for k in range(0, k):
            k = k % 2
            own[k][0] = -prices[0]
            for j in range(1, length):
                own[k][j] = max(own[k][j-1], no_own[k-1][j-1] - prices[j])
                no_own[k][j] = max(no_own[k][j-1], own[k][j-1] + prices[j])
        return max(no_own[0][-1], no_own[1][-1])

    def maxProfit2(self, k, prices):
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

    def test_one(self):
        input = [2, 4, 1]
        self.assertEqual(self.s.maxProfit(2,input), 2)
    
    def test_two(self):
        input = [3, 2, 6, 5, 0, 3]
        self.assertEqual(self.s.maxProfit(2, input), 7)

    def test_three(self):
        input = [1, 2]
        self.assertEqual(self.s.maxProfit(1, input), 1)
if __name__ == "__main__":
    unittest.main()
