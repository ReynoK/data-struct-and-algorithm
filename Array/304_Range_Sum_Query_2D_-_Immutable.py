import unittest


class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        
        self.len_row = len(matrix)

        if self.len_row == 0:
            return

        self.len_col = len(matrix[0])
        self.sum_matrix = [[0]*self.len_col for _ in range(self.len_row)]

        self.sum_matrix[0][0] = matrix[0][0]

        for i in range(1, self.len_col):
            self.sum_matrix[0][i] = self.sum_matrix[0][i-1] + matrix[0][i]

        for i in range(1, self.len_row):
            self.sum_matrix[i][0] = self.sum_matrix[i-1][0] + matrix[i][0]

        for i in range(1, self.len_row):
            for j in range(1, self.len_col):
                self.sum_matrix[i][j] = self.sum_matrix[i-1][j] + self.sum_matrix[i][j-1] - self.sum_matrix[i-1][j-1] + matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        if self.len_row == 0:
            return 0

        sum_ = self.sum_matrix[row2][col2]

        if row1 > 0:
            sum_ -= self.sumRegion(0, col1, row1 - 1, col2)
        
        if col1 > 0:
            sum_ -= self.sumRegion(row1, 0, row2, col1-1)

        if row1>0 and col1 > 0:
            sum_ -= self.sumRegion(0,0,row1-1,col1-1)

        return sum_
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.s = Solution()
        pass

    def test_one(self):
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ]
        obj = NumMatrix(matrix)
        self.assertEqual(obj.sumRegion(2, 1, 4, 3), 8)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
