import unittest


class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        p = 0
        q = 0

        while q < len(t) and p < len(s):
            if t[q] == s[p]:
                p += 1
            
            q += 1
        
        return p == len(s)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertTrue(self.s.isSubsequence('abc', 'ahbgdc'))
    
    def test_two(self):
        self.assertFalse(self.s.isSubsequence('axc', 'ahbgdc'))

if __name__ == "__main__":
    unittest.main()
