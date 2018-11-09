class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums)

        nums = nums[::2]
        return sum(nums)