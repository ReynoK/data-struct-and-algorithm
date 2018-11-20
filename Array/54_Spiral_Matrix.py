import unittest


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        col_length = len(matrix[0])
        row_length = len(matrix)
        ans = []
        c_n = 0

        while True:
            for i in range(c_n, col_length - c_n):
                ans.append(matrix[c_n][i])

            if row_length - c_n - 1 - c_n < 1: 
                break

            for i in range(c_n+1, row_length - c_n):
                ans.append(matrix[i][col_length - c_n - 1])

            if col_length - c_n - 1 - c_n < 1:
                break
            
            for i in range(col_length - c_n - 2, c_n - 1, -1):
                ans.append(matrix[row_length - c_n - 1][i])

            if row_length - c_n - 1 - c_n > 1:
                for i in range(row_length - c_n - 2, c_n, -1):
                    ans.append(matrix[i][c_n])

            c_n += 1

        return ans





class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        print(self.s.spiralOrder(input))
    
    def test_two(self):
        input = [
            [1, 2, 3, 4], 
            [5, 6, 7, 8], 
            [9, 10, 11, 12]]
        print(self.s.spiralOrder(input))

if __name__ == "__main__":
    unittest.main()
