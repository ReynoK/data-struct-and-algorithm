import unittest


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        h = len(nums) - 1

        while l < h-1:
            m = (l + h) // 2

            if nums[m] == nums[l] and nums[m] == nums[h]:
                return min(nums[l:h+1])

            if nums[m] >= nums[l]:
                l = m
            else:
                # 右边有序
                h = m
        return nums[h]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1, 3, 5]
        self.assertEqual(self.s.findMin(input), 1)
    
    def test_two(self):
        input = [2,2,2,0,1]
        self.assertEqual(self.s.findMin(input), 0)

    def test_three(self):
        input = [2, 0, 1,2]
        self.assertEqual(self.s.findMin(input), 0)

if __name__ == "__main__":
    unittest.main()
