import unittest

"""寻找无序数组中，最长递增子序列的个数

思路：动态规划，dp[i] = (x,y)，表示以当前数字为结尾的最长子序列长度，长度为x,数目为y。统计完，累加最长长度的个数即可得出结果
"""


class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length == 0:
            return 0

        dp = [[0,0]] * length

        dp[0] = [1,1]
        max_lis = 1

        for i in range(1, length):
            dp[i] = [0,1]
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[j][0] > dp[i][0]:
                        dp[i] = dp[j][:]
                    elif dp[j][0] == dp[i][0]:
                        dp[i][1] += dp[j][1]
            dp[i][0] += 1
            max_lis = max(dp[i][0], max_lis)
        
        return sum([x[1] for x in dp if x[0] == max_lis])

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1, 3, 5, 4, 7]
        self.assertEqual(self.s.findNumberOfLIS(input), 2)
    
    def test_two(self):
        input = [2, 2, 2, 2, 2]
        self.assertEqual(self.s.findNumberOfLIS(input), 5)

if __name__ == "__main__":
    unittest.main()
