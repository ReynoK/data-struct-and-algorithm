import unittest

"""
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。请注意，顺序不同的序列被视作不同的组合。

思路：因为顺序不同被视为不同的组合，而且给与的数组是不带重复数字的，因此现将数组nums进行排序。假设dp[i]是和为i的所有排列组合，那么对于所有小于target的数，
dp[i] = sum(dp[i-num]) for num in nums if num < i
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        dp = [0]*(target +1 )
        dp[0] = 1
        
        for i in range(1, target+1):
            for num in nums:
                if num > target:
                    break
                
                dp[i] += dp[i - num]
        return dp[-1]

                
                    


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.combinationSum4([1, 2, 3],4), 7)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
