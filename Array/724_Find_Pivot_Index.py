import unittest


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        
        length = len(nums)
        left_sum = [0] * length
        right_sum = [0] * length

        sum_ = 0
        for index in range(length):
            left_sum[index] = sum_
            sum_ += nums[index]
        
        sum_ = 0
        for index in range(length-1,-1,-1):
            right_sum[index] = sum_
            sum_+= nums[index]

        for index in range(length):
            if right_sum[index] == left_sum[index]:
                return index
        return -1 
            

class TestPivotIndex(unittest.TestCase):
    def test_one(self):
        nums = [-1, -1, -1, -1, -1, 0]
        s = Solution()
        self.assertEqual(s.pivotIndex(nums), 2)

    def test_two(self):
        nums = [1, 7, 3, 6, 5, 6]
        s = Solution()
        self.assertEqual(s.pivotIndex(nums), 3)

    def test_three(self):
        nums = [1, 2, 3]
        s = Solution()
        self.assertEqual(s.pivotIndex(nums), -1)

    def test_four(self):
        nums = [-1, -1, 1, 1, 0, 0]
        s = Solution()
        self.assertEqual(s.pivotIndex(nums), 4)

if __name__ == "__main__":
    unittest.main()
