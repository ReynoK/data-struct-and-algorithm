import unittest

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return 0

        count = 1
        length = len(nums)
        max_step = nums[0]
        last_max = 0
        while max_step < length - 1:
            
            count += 1
            temp_max_step = max_step
            
            for index in range(last_max+1, max_step+1):
                temp_max_step = max(temp_max_step, nums[index] + index)

            last_max = max_step
            max_step = temp_max_step

        return count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [2, 3, 1, 1, 4]
        self.assertEqual(self.s.jump(input), 2)

    def test_two(self):
        input = [1,2,3]
        self.assertEqual(self.s.jump(input), 2)

if __name__ == "__main__":
    unittest.main()