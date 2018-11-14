"""判断数组中相同数字之间的距离最大为k
思路：hashmap
"""

class Solution(object):
    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        from collections import defaultdict
        coll = defaultdict(list)

        for index, num in enumerate(nums):
            coll[num].append(index)

        for key, value in coll.items():
            for index in range(1, len(value)):
                if value[index] - value[index-1] <= k:
                    return True

        return False

    def containsNearbyDuplicate(self, nums, k):
        result = {}

        for index,num in enumerate(nums):
            if num in result and index - result[num] <= k:
                return True
            
            result[num] = index

        return False
