import unittest


class Solution:
    def getMoneyAmount2(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def helper(i,j):
            if i >= j:
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]
            res = n*(n+1)/2
            for index in range(i, j+1):
                res = min(res, index + max(helper(i,index-1) , helper(index+1, j)))
            
            cache[(i,j)] = res
            return res

        return helper(1, n)

    def getMoneyAmount(self, n):

        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n,0,-1):
            for j in range(i+1,n+1):
                res = n * (n+1)
                if j == i + 1:
                    dp[i][j] = i
                    continue
                for k in range(i, j):
                    res = min(res, k + max(dp[i][k-1], dp[k+1][j]))
                    
                dp[i][j] = res
        return dp[1][n]
                

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.getMoneyAmount(3), 2)
    
    def test_two(self):
        self.assertEqual(self.s.getMoneyAmount(2), 1)

if __name__ == "__main__":
    unittest.main()
