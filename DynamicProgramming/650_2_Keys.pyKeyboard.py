import unittest

"""类似于动态规划

思路：比如 6 可以是 AAA * 2（那么就是f[3] + 1 copy + 1 paste） 或 AA*3(f[2] + 1 copy + 2 Paste) 或 A*6(f[1] + 1copy + 5 paste)组成，一次内推
Returns:
    [type] -- [description]
"""


class Solution:
    def minSteps2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = i
            for j in range(2, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        
        return dp[n]
    def minSteps(self, n):
        
        cache = {}
        def helper(n):
            if n == 0 or n == 1:
                return 0
            if n in cache:
                return cache[n]
            cache[n] = n

            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    cache[n] = min(cache[n], helper(n//i) + i)
            return cache[n]
        return helper(n)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.minSteps(3),3)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
