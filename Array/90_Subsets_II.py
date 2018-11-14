import unittest

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        subsets = []

        def helper(start, subset):
            if start == len(nums):
                subsets.append(subset)
                return 
            subsets.append(subset)
            for index in range(start, len(nums)):
                if index > start and nums[index] == nums[index-1]:          # 关键点
                    continue
                temp = subset[:]
                temp.append(nums[index])
                helper(index+1, temp)

        helper(0, [])
        return subsets

class TestSubSet(unittest.TestCase):
    def test_one(self):
        input = [1,2,2]
        s = Solution()
        print(s.subsetsWithDup(input))

if __name__ == "__main__":
    unittest.main()