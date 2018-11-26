import unittest


class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0 or N >= K + W:
            return 1
        dp = [0] * (N+1)
        dp[0] = 1
        sum_ = 1.0
        res = 0

        for i in range(1, N+1):
            if i >= W+1:
               sum_ -= dp[i-W-1]            # 超过w之后，要减去之前累加的达不到的 dp[0] dp[1] dp[2]

            dp[i] = sum_/W
            if i < K:
                sum_ += dp[i]

            if i >= K:
                res += dp[i]
           
        return res

    # def new21Game2(self, N, K, W):
    #     if K == 0 or N >= K + W:
    #         return 1
    #     dp = [1.0] + [0.0] * N
    #     Wsum = 1.0
    #     for i in range(1, N + 1):
    #         dp[i] = Wsum / W
    #         if i < K:
    #             Wsum += dp[i]
    #         if i - W >= 0:
    #             Wsum -= dp[i - W]
    #     return sum(dp[K:])

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        print(self.s.new21Game(21,17,10))
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
