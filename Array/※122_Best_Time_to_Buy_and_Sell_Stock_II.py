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

        if len(prices)<2:
            return 0

        max_profit = 0

        sell_price = prices[0]   
        for index in range(1, len(prices)):
            if prices[index] < prices[index - 1]:
                print(index,(prices[index-1] - sell_price))
                max_profit += (prices[index-1] - sell_price)
                sell_price = prices[index]
        max_profit += (prices[-1] - sell_price)

        return max_profit


class TestSolution(unittest.TestCase):
    def test_one(self):
        prices = [7,1,5,3,6,4]
        s = Solution()
        print(s.maxProfit(prices))


if __name__ == "__main__":
    unittest.main()
        
            
        