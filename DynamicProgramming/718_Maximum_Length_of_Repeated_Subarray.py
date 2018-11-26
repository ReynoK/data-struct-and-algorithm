import unittest

"""寻找公共最长子串

思路：用dp[i][j]表示以A[i]和B[j]为子串的末尾，那么以改点为末尾的子串长度由dp[i-1][j-1]决定
"""


class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        a_len = len(A)
        b_len = len(B)
        dp = [[0] * (b_len + 1) for _ in range(b_len + 1) ]

        for i in range(a_len):
            for j in range(b_len):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
        
        return max([max(row) for row in dp])

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]), 3)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
