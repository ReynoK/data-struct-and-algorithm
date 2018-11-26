import unittest

"""知一个 NxN 的国际象棋棋盘，棋盘的行号和列号都是从 0 开始。即最左上角的格子记为 (0, 0)，最右下角的记为 (N-1, N-1)。 

现有一个 “马”（也译作 “骑士”）位于 (r, c) ，并打算进行 K 次移动。 

如下图所示，国际象棋的 “马” 每一步先沿水平或垂直方向移动 2 个格子，然后向与之相垂直的方向再移动 1 个格子，共有 8 个可选的位置。

现在 “马” 每一步都从可选的位置（包括棋盘外部的）中独立随机地选择一个进行移动，直到移动了 K 次或跳到了棋盘外面。

求移动结束后，“马” 仍留在棋盘上的概率。

思路：计算每个空格第k步仍然留在棋盘上概率，由周围第k-1步仍留在期盼的概率所得出
"""


class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """

        dp = [[1]*N for _ in range(N)]
        for k in range(K):
            dp_tmp = [[1]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    res = 0
                    if i - 2 >= 0:
                        if j - 1 >= 0:
                            res += 1.0/8 * dp[i-2][j-1]

                        if j + 1 < N:
                            res += 1.0/8 * dp[i-2][j+1]

                    if i + 2 < N:
                        if j - 1 >= 0:
                            res += 1.0/8 * dp[i+2][j-1]

                        if j + 1 < N:
                            res += 1.0/8 * dp[i+2][j+1]

                    if j - 2 >= 0:
                        if i - 1>= 0:
                            res += 1.0/8 * dp[i-1][j-2]
                        if i + 1 < N:
                            res += 1.0/8 * dp[i+1][j-2]

                    if j + 2 < N:
                        if i - 1 >= 0:
                            res += 1.0/8 * dp[i-1][j+2]
                        if i + 1 < N:
                            res += 1.0/8 * dp[i+1][j+2]
                    dp_tmp[i][j] = res
            dp = dp_tmp
        return dp[r][c]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.knightProbability(3,2,0,0), 0.0625)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
