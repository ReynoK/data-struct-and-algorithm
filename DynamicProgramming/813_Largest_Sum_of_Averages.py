import unittest


class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        dp = [[0]*(len(A)) for _ in range(K+1) ]

        for i in range(len(A)):
            dp[1][i] = average(A, i, len(A))

        for k in range(2, K+1):
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    dp[k][i] = max(dp[k][i], (P[j] - P[i]) /float(j - i) + dp[k-1][j])
        return dp[K][0]
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.largestSumOfAverages([9, 1, 2, 3, 9], 3), 20)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
