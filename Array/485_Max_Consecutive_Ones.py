"""统计数组中连续1的最长个数
注意点：主义尾部为1的场景

Returns:
    [type] -- [description]
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = 0
        cnt = 0
        flag = False

        for num in nums:
            if num == 0 and flag:
                if cnt > max_:
                    max_ = cnt
                    cnt = 0
                flag = False
            
            if num == 1:
                if flag == True:
                    cnt+=1
                else:
                    flag = True
                    cnt = 1

        if cnt > max_:
            max_ = cnt
        return max_