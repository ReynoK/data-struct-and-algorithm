class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        row_num = len(nums)

        if row_num == 0:
            return nums
        
        col_num = len(nums[0])

        if col_num * row_num != r * c:
            return nums

        result = []
        for i in range(r):
            row = []
            for j in range(c):
                index = i*c + j
                row.append(nums[index//col_num][index%col_num])
            
            result.append(row)

    return result