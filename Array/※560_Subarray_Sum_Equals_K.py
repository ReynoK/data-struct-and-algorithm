"""求连续子数组和为k的个数

思想：累加和，利用累加和可以快速求出某个子数组的和

1. 求0到index的累加和，那么i到j的子数组和等于sum[i] - sum[j]
2. 更进一步，求出sum[i]的和，看sum[i]-k在前面存在的次数，因为sum[i]-(sum[i]-k) = k，这样可以快速计算出次数

Returns:
    [type] -- [description]
"""


import unittest
from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        sum_hash = defaultdict(lambda:0)
        sum_hash[0] = 1
        sum_ = 0
        count = 0

        for num in nums:
            sum_ += num
            count += sum_hash[sum_-k]
            sum_hash[sum_] += 1

        return count

    def subarraySum2(self, nums, k):
        """
        Time limit
        """
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sum_ = [0]
        count = 0

        for i in range(1, len(nums)+1):                 # 终止条件
            sum_.append(nums[i-1] + sum_[i-1])

        for i in range(len(sum_)):
            for j in range(i+1, len(sum_)):
                if sum_[j] - sum_[i] == k:
                    count +=1

        return count

class TestSubarraySum(unittest.TestCase):
    def test_one(self):
        input = [1,1,1]
        s = Solution()
        self.assertEqual(s.subarraySum(input, 2), 2)


if __name__ == "__main__":
    unittest.main()

