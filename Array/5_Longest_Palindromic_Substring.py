import unittest


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or len(s) == 0:
            return ""

        substr = ""

        for i,_ in enumerate(s):
            left = i
            right = i
            while left>=0 and right <len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1

            if length > len(substr):
                substr = s[left+1:right]

            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1

            if length > len(substr):
                substr = s[left+1:right]
            
        return substr

        

        
                

    


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.longestPalindrome("babad"), 'bab')
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
