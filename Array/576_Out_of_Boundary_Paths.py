import unittest


class Solution:
    def findPaths2(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        M = 1000000000 + 7
        matrix = [[0]*n for _ in range(m)]
        res = 0
        matrix[i][j] = 1    

        for _ in range(N):
            matrix_tmp = [[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        res = (res+matrix[i][j]) % M
                    if i == m - 1:
                        res = (res+matrix[i][j]) % M
                    if j == 0:
                        res = (res+matrix[i][j]) % M
                    if j == n - 1:
                        res = (res+matrix[i][j]) % M
                    
                    if i > 0:
                        matrix_tmp[i][j] = (matrix_tmp[i][j] + matrix[i-1][j]) % M
                    if i < m-1:
                        matrix_tmp[i][j] = (matrix_tmp[i][j] + matrix[i+1][j]) % M
                    if j > 0:
                        matrix_tmp[i][j] = (matrix_tmp[i][j] + matrix[i][j-1]) % M
                    if j < n - 1:
                        matrix_tmp[i][j] = (matrix_tmp[i][j] + matrix[i][j+1]) % M

            matrix = matrix_tmp
        return res

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        M = (10**9)+7
        
        cache = {}

        def helper(i,j,count):
            if i < 0 or j <0 or i >=m or j >=n:
                return 1

            if count == 0:
                return count

            if (i, j, count) in cache:
                return cache[(i, j, count)]
            
            up = helper(i-1, j, count-1) % M
            down = helper(i+1, j, count-1) % M
            left = helper(i, j-1, count-1) % M
            right = helper(i, j+1, count-1) % M

            cache[(i, j, count)] = (up + down + left + right) % M

            return cache[(i, j, count)]

        return helper(i,j,N)

                        
                    



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.findPaths(1,3,3,0,1),12)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
