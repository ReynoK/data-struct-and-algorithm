class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        subtracts = [-1]

        for i in range(1, len(nums)):
            subtracts.append(nums[i] - nums[i-1])

        
        
        
