class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        degree = 0
        min_length = len(nums)
        collect = dict()
        for index,num in enumerate(nums):
            if num not in collect:
                collect[num] = [index,index,1]
            else:
                collect[num][1] = index
                collect[num][2] += 1
                degree = max(degree, collect[num][2])
        
        for num,value in collect.items():
            if value[2] < degree:
                continue
            else:
                min_length = min(min_length, value[1] - value[0] + 1)
        
        return min_length
        

s = Solution()
print(s.findShortestSubArray([1,2,2,3,1]))