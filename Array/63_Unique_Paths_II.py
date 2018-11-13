import unittest

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:          # 判断条件
            return 0
        result = [1] + [0] * (len(obstacleGrid[0]) - 1)                                             # 第一步要为1，否则后面计算出来的都是0，因为上面的判断避免了1的存在

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    result[j] = 0
                else:
                    if j > 0:
                        result[j] = result[j] + result[j-1]
        return result[-1]                    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]

        self.assertEqual(self.s.uniquePathsWithObstacles(input), 2)
        
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
