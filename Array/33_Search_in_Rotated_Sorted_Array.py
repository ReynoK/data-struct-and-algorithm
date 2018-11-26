import unittest

class Solution:
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if len(nums) == 0:
        return -1

    l,h = 0,len(nums) -1
    
    while l <= h:
        mid = l + (h-l)//2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            # 左边有序
            if target >= nums[l] and target < nums[mid]:
                h = mid -1
            else:
                l = mid + 1
        else:
            # 右边有序
            if target > nums[mid] and target <= nums[h]:
                l = mid + 1
            else:
                h = mid - 1
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