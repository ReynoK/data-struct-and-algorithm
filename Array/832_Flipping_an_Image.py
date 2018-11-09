class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for row_index, row in enumerate(A):
            temp = []
            for index in range(len(row)-1, -1, -1):
                if row[index] == 0:
                    temp.append(1)
                else:
                    temp.append(0)
            A[row_index] = temp
        return A