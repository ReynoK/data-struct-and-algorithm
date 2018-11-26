import unittest

"""寻找p中非空的连续子串在无限循环'abcd....zabc'中出现的数目

思路：子串计算方式，若当前字符与前面一个字符是连续字符，那么以该字符为结尾的子串数目是在以前一个字符为结尾的子字符串数目加1，否则本身算是一个子串，由于题目要求是无重复的，
因此，另外寻一个bucket表示以该字符为结尾的子串最长长度，依次统计，最后相加。
"""


class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        
        if len(p) < 2:
            return len(p)

        from collections import defaultdict
        coll = defaultdict(lambda:0)

        dp = [0] * len(p)
        dp[0] = 1
        coll[p[0]] = 1

        for i in range(1, len(p)):
            diff = ord(p[i]) - ord(p[i-1])
            if diff == 1 or diff == (ord('a') - ord('z')):
                dp[i] += (dp[i-1]+1)
            else:
                dp[i] = 1
            
            coll[p[i]] = max(coll[p[i]], dp[i])              # 本身也可以占一个
        return sum(coll.values())

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.findSubstringInWraproundString("a"),1)
    
    def test_two(self):
        self.assertEqual(self.s.findSubstringInWraproundString("cac"), 2)

    def test_three(self):
        self.assertEqual(self.s.findSubstringInWraproundString('zab'), 6)

if __name__ == "__main__":
    unittest.main()
