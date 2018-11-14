"""求子集
思路：递归,回溯
注意点：注意终止条件
"""


import unittest

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [nums]+[[]]           # 单个数的子集，还包括空
        nums.sort()
        result = [[]]

        for index,num in enumerate(nums):
            subsets = self.subsets(nums[index+1:])
            for subset in subsets:
                result.append([num] + subset)

        return result


class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        print(s.subsets([]))

if __name__ == "__main__":
    unittest.main()