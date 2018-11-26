import unittest

"""
求要是字符串A和B相等要删除A和B中字符的最小和

思路：令dp[i][j]表示 A[:i+1]和B[i+1]要删除的字符串最小和，如果A[i+1] == B[i+1]表示这个字符可以不删除，那么取决与dp[i-1]和dp[j-1]，如果不等，那么就要删除其中一个，继续寻找，就是
dp[i][j] = 删除A[i+1]的情况下和删除B[i+1]的情况下的最小值，min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

"""


class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
        length_a = len(s1)
        length_b = len(s2)

        dp = [[0]*(length_b+1) for _ in range(length_a+1)]
        for index,s in enumerate(s1):
            dp[index+1][0] = ord(s) + dp[index][0]

        for index,s in enumerate(s2):
            dp[0][index+1] = ord(s) + dp[0][index]

        for i in range(1, length_a+1):
            for j in range(1, length_b+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        return dp[-1][-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.minimumDeleteSum('sea','eat'), 231)
    
    def test_two(self):
        self.assertEqual(self.s.minimumDeleteSum("delete", "leet"), 403)

if __name__ == "__main__":
    unittest.main()
