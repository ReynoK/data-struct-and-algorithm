import unittest


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        
        dp = [[float('inf')]*(100) for _ in range(2)]

        for flight in flights:
            if flight[0] == src:
                dp[0][flight[1]] = flight[2]
        res = dp[0][dst]

        for k in range(1, K+1):
            k = k % 2
            for flight in flights:
                if dp[k-1][flight[0]] < float('inf'):
                    dp[k][flight[1]] = min(dp[k-1][flight[0]] + flight[2], dp[k][flight[1]])
            res = min(res, dp[k][dst])
        return res if res < float('inf') else -1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.findCheapestPrice(
            3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0,2,0), 500)
    
    def test_two(self):
        self.assertEqual(self.s.findCheapestPrice(
            3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0,2,1), 200)

    def test_three(self):
        self.assertEqual(self.s.findCheapestPrice(
            5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],2,1,1), -1)

if __name__ == "__main__":
    unittest.main()
