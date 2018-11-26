import unittest

"""字符串以空格分割成单词后，单词全部在给与的数组中出现，返回True

假设dp[i]表示以该字母为结尾的单词能够被空格分割，那么在(dp[j]=True, j < i)中，至少存在一个j，对于s[j:i+1]会在wordDict中出现

"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0:
            return True

        if len(wordDict) == 0:
            return False

        dp = [False] * (len(s)+1)
        dp[0] = True

        max_length = max([len(w) for w in wordDict])            # 优化

        for i in range(1, len(s)+1):
            for j in range(max(0, i-max_length), i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    continue
        return dp[-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.wordBreak("leetcode", ["leet", "code"]), True)
    
    def test_two(self):
        self.assertTrue(self.s.wordBreak("applepenapple", ["apple", "pen"]))

    def test_three(self):
        self.assertFalse(self.s.wordBreak(
            "catsandog", ["cats", "dog", "sand", "and", "cat"]))

if __name__ == "__main__":
    unittest.main()
