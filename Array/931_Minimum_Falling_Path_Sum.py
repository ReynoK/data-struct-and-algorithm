import unittest


class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
        if len(A) == 0:
            return 0
        length = len(A)
        dp = [ [0]*length for i in range(2)] 
        for index,num in enumerate(A[0]):
            dp[0][index] = num

        for k in range(1, length):
            i = k%2
            for j in range(0, length):
                if j == 0:
                    dp[i][j] = min(dp[i-1][:2]) + A[k][j]
                elif j == length - 1:
                    dp[i][j] = min(dp[i-1][-2:]) + A[k][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1:j+2]) + A[k][j]
        return min(dp[(length-1)%2][:])



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.s.minFallingPathSum(input), 12)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
