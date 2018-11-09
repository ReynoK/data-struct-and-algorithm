class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


        l = 0
        h = len(nums) - 1

        while l < h:
            while l < h and nums[l] != 0:
                l += 1

            while l < h and nums[h] == 0:
                h -= 1

            if l<h:
                nums[l],nums[h] = nums[h],nums[l]
                

        
                