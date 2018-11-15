import unittest


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums[:])

        rob_first_condition = [0] * len(nums)
        no_rob_first_condition = [0] * len(nums)

        rob_first_condition[0] = nums[0]
        rob_first_condition[1] = max(nums[:2])
        no_rob_first_condition[1] = nums[1]

        for i in range(1, len(nums) - 1):
            rob_first_condition[i] = max(rob_first_condition[i-1], rob_first_condition[i-2] + nums[i])
            no_rob_first_condition[i] = max(no_rob_first_condition[i-1], no_rob_first_condition[i-2] + nums[i])

        rob_first_condition[-1] = max(rob_first_condition[-2], rob_first_condition[-3])
        no_rob_first_condition[-1] = max(no_rob_first_condition[-2], no_rob_first_condition[-3] + nums[-1])

        return max(rob_first_condition[-1], no_rob_first_condition[-1])

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [2, 3, 2]
        self.assertEqual(self.s.rob(input), 3)
    
    def test_two(self):
        input = [1,2,3,1]
        self.assertEqual(self.s.rob(input), 4)

if __name__ == "__main__":
    unittest.main()
