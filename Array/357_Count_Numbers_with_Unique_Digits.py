import unittest


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1] = 10

        for i in range(2, n+1):



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        pass
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
