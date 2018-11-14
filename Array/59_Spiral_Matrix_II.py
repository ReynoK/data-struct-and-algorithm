import unittest


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if n == 0:
            return []

        matrix = [[0 for j in range(n)] for i in range(n)]

        start = 1
        for circle_index in range((n+1)//2):

            for i in range(circle_index, n - circle_index):
                matrix[circle_index][i] = start
                start += 1
            if n - circle_index - 1 != circle_index:
                for i in range(circle_index + 1, n - circle_index - 1):
                    matrix[i][n-circle_index-1] = start
                    start += 1
            if n - circle_index - 1 != circle_index:
                for i in range(n - circle_index-1, circle_index-1, -1 ):
                    matrix[n-circle_index-1][i] = start
                    start += 1

            if n - circle_index - 1 != circle_index:
                for i in range(n-circle_index-2, circle_index, -1):
                    matrix[i][circle_index] = start
                    start += 1

        return matrix

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        result = self.s.generateMatrix(3)

        right_result = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]

        self.assertEqual(result, right_result)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
