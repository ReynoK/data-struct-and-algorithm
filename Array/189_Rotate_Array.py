import unittest


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k , len(nums)-1)
        return None

    def reverse(self, nums, start, end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1,2,3,4,5]
        self.s.rotate(input, 2)
        self.assertEqual(input, [4,5,1,2,3])
    
    def test_two(self):
        input = [1,2,3,4,5]
        self.s.rotate(input, 7)
        self.assertEqual(input, [4,5,1,2,3])

if __name__ == "__main__":
    unittest.main()
