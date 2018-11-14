import unittest

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if len(grid) == 0:
            return 0

        def helper(i,j):
            if grid[i][j] != 1:
                return 0
            grid[i][j] = -1
            area = 1
            if i > 0:
                area += helper(i-1, j)
            if j > 0:
                area += helper(i, j-1)
            if i < len(grid)-1:
                area += helper(i+1, j)
            if j < len(grid[0]) - 1:
                area += helper(i, j+ 1)
            
            return area

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, helper(i,j))
        return max_area

class TestMaxArea(unittest.TestCase):
    def test_one(self):
        input = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

        s = Solution()
        print(s.maxAreaOfIsland(input))

    def test_zero(self):
        input = [[0, 0, 0, 0, 0, 0, 0, 0]]
        s = Solution()
        self.assertEqual(s.maxAreaOfIsland(input), 0)

if __name__ == "__main__":
    unittest.main()
