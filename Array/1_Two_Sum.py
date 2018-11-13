import unittest

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
            another = target - key

            if another == key and len(dis[key]) > 1:
                return dis[key][:2]
            
            if another in dis:
                return [dis[key][0], dis[another][0]]

class TestTwoSum(unittest.TestCase):
    def test_one(self):
        nums = [2, 7, 11, 15]
        s = Solution()
        print(s.twoSum(nums, 9))

if __name__ == "__main__":
    unittest.main()
