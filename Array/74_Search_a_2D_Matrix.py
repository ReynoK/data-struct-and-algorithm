"""在每行是顺序排序，每行第一个元素大于上一行的最后一个元素中寻找指定数字

思路：二分法
1. 先按第一列二分，找出行的位置（考虑好指针的落点），然后在列中再使用二分查找
2. 拉平矩阵，按照普通的二分法来查找

Returns:
    [type] -- [description]
"""


import unittest

class Solution:
    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        l = 0
        h = len(matrix) - 1

        while l < h:
            m = (l + h) // 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                h = m - 1
            else:
                l = m + 1

        if matrix[l][0] > target:
            l -= 1

        if l >= 0:
            r_l = 0
            r_h = len(matrix[l]) - 1
            while r_l <= r_h:
                m = (r_l + r_h) // 2
                if matrix[l][m] == target:
                    return True
                elif matrix[l][m] > target:
                    r_h = m - 1
                else:
                    r_l = m + 1
        return False

    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        l = 0
        h = len(matrix) * len(matrix[0]) - 1

        while l<=h:
            m = (l+h)//2
            num = matrix[m//len(matrix[0])][m%len(matrix[0])]

            if num == target:
                return True
            elif num < target:
                l = m + 1
            else:
                h = m - 1
        return False

class TestSearchMatrix(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]

        target = 3

        self.assertTrue(self.s.searchMatrix(input, target))


    def test_two(self):
        input = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]

        target = 13

        self.assertFalse(self.s.searchMatrix(input,target))


    def test_three(self):
        input = [[1]]
        target = 2
        self.assertFalse(self.s.searchMatrix(input, target))

if __name__ == "__main__":
    unittest.main()
