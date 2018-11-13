"""将有的0行列都置为0，要求常数空间

思路：利用首行和首列来存储数据

Returns:
    [type] -- [description]
"""



import unittest


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """ 
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        zero_row = 1
        zero_col = 1
        for num in matrix[0]:
            zero_row *= num
        for i in range(len(matrix)):
            zero_col *= matrix[i][0]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if zero_row == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        if zero_col == 0:
            for j in range(len(matrix)):
                matrix[j][0] = 0

        return None


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        output = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]


        self.s.setZeroes(input)
        self.assertEqual(input, output)

    
    def test_two(self):
        input = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]

        output = [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ]

        self.s.setZeroes(input)

        self.assertEqual(input, output)

if __name__ == "__main__":
    unittest.main()
