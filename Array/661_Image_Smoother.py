class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        h = len(M)
        c = len(M[0])

        new_M = []
        for _ in len(h):
            new_M.append([0]*c)

        for i in range(h):
            for j in range(c):
                sum_ =M[i][j]
                cnt = 1

                if i-1 > 0:
                    if j - 1 > 0:
                        cnt += 1
                    sum_ += M[i-1][j-1] if j-1>0 else 0
                    sum_ += M[i-1][j]
                    sum_ += M[i-1][j+1] if j+1 < c else 0

                sum_ += M[i][j-1] if j-1 > 0 else 0
                sum_ += M[i][j+1] if j+1 < c else 0

                if i+1 < h:
                    sum_ += M[i+1][j-1] if j-1 > 0 else 0
                    sum_ += M[i+1][j]
                    sum_ += M[i+1][j+1] if j+1 < c else 0
                 
            new_M[i][j] = 

