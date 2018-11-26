import unittest


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        max_res = 0

        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = 0
                
                if matrix[i][j] == '1':
                    res = 1

                    if i > 0 and j>0 and dp[i-1][j-1] > 0:
                        left_up = dp[i-1][j-1]
                        index = 1

                        while index <= left_up and i - index >= 0 and j - index >= 0 and matrix[i-index][j] == '1' and matrix[i][j-index] == '1':
                            res += 1
                            index += 1

                dp[i][j] = res
                max_res = max(max_res, dp[i][j])
        return max_res**2


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [["1", "1", "1", "1"], [
            "1", "1", "1", "1"], ["1", "1", "1", "1"]]

        self.assertEqual(self.s.maximalSquare(input), 9)
            
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
