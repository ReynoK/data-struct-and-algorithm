"""寻找最短路径

思路：动态规划，非递归和递归均可
Returns:
    [type] -- [description]
"""


import unittest


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        w = len(grid[0]) 
        cache = [grid[0][0]]
        for index in range(1,len(grid[0])):
            cache.append(grid[0][index] + cache[index-1])

        for i in range(1,len(grid)):
            for j in range(w):
                if j == 0:
                    cache[0] = grid[i][j] + cache[0]
                else:
                    cache[j] = grid[i][j] + min(cache[j-1], cache[j])
        return cache[-1]

class TestMinPathSum(unittest.TestCase):
    def test_one(self):
        input = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        s = Solution()
        print(s.minPathSum(input))

if __name__ == "__main__":
    unittest.main()
                    
