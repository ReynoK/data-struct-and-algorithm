import unittest


class Solution:
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        length = len(prices)
        own = [0] * length
        no_own = [0] * length

        own[0] = -prices[0]
        own[1]  = max(-prices[0], -prices[1])
        no_own[1] = max(no_own[0], own[0] + prices[1])          # 要初始化 no_own[1]

        for i in range(2,length):
            own[i] = max(own[i-1], no_own[i-2] - prices[i])
            no_own[i] = max(no_own[i-1], own[i-1] + prices[i])
        return no_own[-1]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        length = len(prices)

        last_own = -prices[0]
        last_no_own = 0
        last_2_no_own = 0

        for i in range(1, length):
            own = max(last_own, last_2_no_own - prices[i])
            no_own = max(last_no_own, last_own + prices[i])

            last_2_no_own = last_no_own
            last_no_own = no_own
            last_own = own
        return last_no_own


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
