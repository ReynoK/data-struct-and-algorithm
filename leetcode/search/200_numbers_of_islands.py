"""
思路：将搜寻过的 1 置为 #，表示其属于某一个已经寻找的岛屿
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        sum = 0

        if len(grid) == 0 or len(grid[0]) == 0:
            return sum

        n,m = len(grid), len(grid[0])

        def helper(i,j):
            if grid[i][j] == '0' or grid[i][j] == '#':
                return 
            else:
                grid[i][j] = '#'

            #up
            if i > 0:
                helper(i-1,j)

            #left
            if j > 0:
                helper(i, j - 1)
            #down
            if i < n-1:
                helper(i+1, j)
            #right
            if j < m - 1:
                helper(i, j+1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    sum += 1
                    helper(i,j)
                else:
                    continue

        return sum


s = Solution()
grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]


print(s.numIslands(grid))