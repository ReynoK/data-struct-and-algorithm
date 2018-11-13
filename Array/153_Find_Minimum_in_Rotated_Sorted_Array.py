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

        while l <= h:
            m = (l + h) // 2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            
            if nums[m]< nums[m-1]:
                return nums[m]

            if nums[m] > nums[0]:
                l = m + 1
            else:
                h = m - 1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [4,5,6,1,2,3]
        self.assertEqual(self.s.findMin(input), 1)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
