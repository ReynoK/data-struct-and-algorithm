import unittest


class Solution(object):
    def longestPalindromeSubseq(self, s):
        length = len(s)

        if length == 0:
            return 0

        dp = [[0]*(length) for _ in range(length)]

        for i in range(length-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][-1]




    def longestPalindromeSubseq2(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        def helper(str_a, str_b):

            len_a = len(str_a)
            len_b = len(str_b)

            if len_a == 0 or len_b == 0:
                return 0

            str_b = str_b[::-1]

            dp = [[0]*(len_b+1) for _ in range(len_a+1)]

            for i in range(1, len_a+1):
                for j in range(1, len_b+1):
                    if str_a[i-1] == str_b[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp[-1][-1] * 2

        res = 1

        for index, str in enumerate(s):
            res = max(res, max(helper(s[:index], s[index+1:]) + 1, helper(s[:index+1], s[index+1:])))

        return res

                    


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.longestPalindromeSubseq("bbbab"), 4)
    
    def test_two(self):
        self.assertEqual(self.s.longestPalindromeSubseq("cbbd"), 2)

if __name__ == "__main__":
    unittest.main()
