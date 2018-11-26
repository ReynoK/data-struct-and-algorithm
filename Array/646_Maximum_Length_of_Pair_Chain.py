import unittest


class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()

        dp = [0] * len(pairs)

        for i in range(len(pairs)):
            dp[i] = 0
            for j in range(0, i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j])

            dp[i] += 1

        return max(dp)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.findLongestChain([[1, 2], [2, 3], [3, 4]]), 2)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
