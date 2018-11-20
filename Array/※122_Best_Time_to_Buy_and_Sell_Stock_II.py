"""买卖股票二，可多次买卖

思路：寻找分段的波峰波谷
Returns:
    [type] -- [description]
"""


import unittest

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        own = [0] * len(prices)
        no_own = [0] * len(prices)
        own[0] = -prices[0]

        for i in range(1, len(prices)):
            own[i] = max(own[i-1], no_own[i-1] - prices[i])
            no_own[i] = max(no_own[i-1], own[i] + prices[i])

        return no_own[-1]
                

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices)<2:
            return 0

        max_profit = 0

        sell_price = prices[0]   
        for index in range(1, len(prices)):
            if prices[index] < prices[index - 1]:
                max_profit += (prices[index-1] - sell_price)
                sell_price = prices[index]
        max_profit += (prices[-1] - sell_price)

        return max_profit


class TestSolution(unittest.TestCase):
    def test_one(self):
        prices = [7,1,5,3,6,4]
        s = Solution()
        print(s.maxProfit(prices))

    def test_two(self):
        prices = [1, 2, 3, 4, 5]
        s = Solution()
        print(s.maxProfit(prices))


if __name__ == "__main__":
    unittest.main()
        
            
        
