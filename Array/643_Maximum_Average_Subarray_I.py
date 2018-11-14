"""寻找数组连续k个数字，其平均值最大

思路：没有特殊技巧，就是简单求和，一个方便的方式是减前一个被移除窗口，加新被加入窗口的值，减少计算量
注意点：要的是浮点数，需要转换

Returns:
    [type] -- [description]
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        sum_ = max_sum = sum(nums[:k])
        index = k

        while index < len(nums):
            sum_ = sum_ - nums[index-k] + nums[index]
            max_sum = max(sum_, max_sum)
            index += 1

        return float(max_sum)/k
