import unittest


class Solution:
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    h = len(nums) - 1

    while l <= h:
        m = (l + h) // 2
        if nums[m] == target:
            return m
        
        if nums[m] >= nums[l]:
            if target >= nums[l] and target < nums[m]:
                h = m - 1
            else:
                l = m + 1
        else:
            if target> nums[m] and target <= nums[h]:
                l = m + 1
            else:
                h = m - 1

    return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    
    def test_one(self):
        input = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.s.search(input, target), 4)

    def test_two(self):
        input = [4,5,6,7,0,1,2]
        target = 8
        self.assertEqual(self.s.search(input, target), -1)
    def test_three(self):
        input = [3,1]
        target = 1
        self.assertEqual(self.s.search(input, target), 1)

if __name__ == "__main__":
    unittest.main()