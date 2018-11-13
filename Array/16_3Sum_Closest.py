import unittest


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = nums.sort()

        p = 0
        q = len(nums) - 1 
        r = 