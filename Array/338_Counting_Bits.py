import unittest


class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)
        if num == 0:
            return dp
        
        dp[1] = 1
        step = 1

        for i in range(2, num+1):
            if i % step == 0:
                step *= 2
            dp[i] = dp[i-step] +1
        return dp
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.countBits(2), [0,1,1])
    
    def test_two(self):
        self.assertEqual(self.s.countBits(5), [0, 1, 1, 2, 1, 2])

if __name__ == "__main__":
    unittest.main()
