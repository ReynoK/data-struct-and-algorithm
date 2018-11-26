import unittest

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        postive_arr = [1] * len(nums)
        minus_arr = [1] * len(nums)

        postive_arr[0] = minus_arr[0] = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > 0:
                postive_arr[i] = max(postive_arr[i-1]*nums[i], nums[i])
                minus_arr[i] = min(minus_arr[i-1]*nums[i], nums[i])
            elif nums[i] < 0:
                minus_arr[i] = min(postive_arr[i-1]*nums[i], nums[i])
                postive_arr[i] = max(minus_arr[i-1]*nums[i], nums[i])
            else:
                postive_arr[i] = minus_arr[i] = 0

        return max(postive_arr)
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [2, 3, -2, 4]
        self.assertEqual(self.s.maxProduct(input), 6)
    
    def test_two(self):
        input = [-2, 0, -1]
        self.assertEqual(self.s.maxProduct(input), 0)

if __name__ == "__main__":
    unittest.main()
