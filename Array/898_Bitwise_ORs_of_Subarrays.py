import unittest


class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        length = len(A)

        if length == 0:
            return 0
        res_set = set()

        dp = [[0]*length for _ in range(length)]


        for i in range(length):
            dp[i][i] = A[i]
            res_set.add(dp[i][i])
            for j in range(i+1, length):
                dp[i][j] = dp[i][j-1] | A[j]
                res_set.add(dp[i][j])

        return len(res_set)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.subarrayBitwiseORs([1, 1, 2]), 3)
    
    def test_two(self):
        self.assertEqual(self.s.subarrayBitwiseORs([1, 2, 4]), 6)

if __name__ == "__main__":
    unittest.main()
