import unittest

"""寻找子集，使得子集中si%sj == 0  sj%si==0

思路：排序，每个数字num[i]为结尾的所能组成的子集为max(dp[j] for j < i if num[i]%num[j] == 0) + 1
"""


class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        length = len(nums)

        if length < 2:
            return nums

        nums.sort()
        dp = [[1,i] for i in range(length)]

        for i in range(1, length):
            res = 0
            cor = i
            for j in range(0,i):
                if nums[i] % nums[j] == 0:
                    if dp[j][0] > res:
                        res = dp[j][0]
                        cor = j
            dp[i] = [res+1, cor]
        max_index = 0
        max_sub = 0
        for index,item in enumerate(dp):
            if item[0] > max_sub:
                max_sub = item[0]
                max_index = index

        subset = []
        while True:
            subset.insert(0, nums[max_index])
            next_max_index = dp[max_index][1]
            if next_max_index == max_index:
                break
            max_index = next_max_index

        return subset


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        print(self.s.largestDivisibleSubset([1, 2, 3]))

    def test_two(self):
        print(self.s.largestDivisibleSubset([1, 2, 4, 8]))

if __name__ == "__main__":
    unittest.main()
