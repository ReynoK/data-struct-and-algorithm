class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        from collections import defaultdict
        dis = defaultdict(list)
        for index,num in enumerate(nums):
            dis[num].append(index)

        for key in dis.keys():
            