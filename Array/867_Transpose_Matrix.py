class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        row_num = len(A)
        
        if row_num == 0:
            return A

        col_num = len(A[0])

        if col_num == 0:
            return A

        new_martrix = []
        for _ in range(col_num):
            new_martrix.append([])

        for i in range(row_num):
            for j in range(col_num):
                new_martrix[j].append(A[i][j])
        
        return new_martrix