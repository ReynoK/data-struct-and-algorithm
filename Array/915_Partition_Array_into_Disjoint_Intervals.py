"""寻找切割点，使得左边子数组的值都小于等于右边子数组，要求该切割点最小

思路：
1. 即左边数组的最大值要小于或等于右边数组的最小值，那么分别统计每个位置左边数组的最大值，每个位置右边数组的最小值，然后遍历比较，符号条件的就是切割点
2. 从切割点当前来看，每次遍历左边的最大值应该小于或等于当前值，若左边的极值大于则表示该点不是切割点，应该继续往前
Returns:
    [type] -- [description]
"""


import unittest


class Solution(object):
    def partitionDisjoint2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0

        max_left = []
        max_num = A[0]

        for num in A:
            max_num = max(max_num, num)
            max_left.append(max_num)

        min_right = [0] * len(A)
        min_num = A[-1]

        for index in range(len(A)-1, -1, -1):
            min_num = min(min_num, A[index])
            min_right[index] = min_num

        for index in range(len(A)-1):
            if max_left[index] <= min_right[index + 1]:
                return index + 1

    def partitionDisjoint(self, A):
        if len(A) == 0:
            return 0

        local_max = A[0]
        left_max = A[0]
        partition = 0
        for index in range(1, len(A)):
            if A[index] < local_max:
                partition = index
                local_max = left_max
            else:
                left_max = max(A[index], left_max)

        return partition + 1





class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [5, 0, 3, 8, 6]
        self.assertEqual(self.s.partitionDisjoint(input), 3)
    
    def test_two(self):
        input = [1, 1, 1, 0, 6, 12]
        self.assertEqual(self.s.partitionDisjoint(input), 4)

if __name__ == "__main__":
    unittest.main()
