import unittest


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left_sum = sum(nums[:-1])
        right_sum = 0

        if left_sum == right_sum:
            return len(nums) - 1

        for index in range(len(nums)-2, -1,-1):
            left_sum -= nums[index+1]
            right_sum += nums[index+1]
            print(left_sum,right_sum)
            if left_sum == right_sum:
                return index

        return -1

class TestPivotIndex(unittest.TestCase):
    def test_one(self):
        nums = [-1, -1, -1, -1, -1, 0]
        s = Solution()
        print(s.pivotIndex(nums))

if __name__ == "__main__":
    unittest.main()
