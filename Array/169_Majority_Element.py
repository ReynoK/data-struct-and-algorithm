class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        from collections import defaultdict

        result = defaultdict(lambda:0)

        for num in nums:
            result[num] += 1

        for num,cnt in result.items():
            if cnt > len(nums)//2:
                return num