import unittest


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        l = 0
        h = len(nums) - 1

        while l < h:
            while l < h and nums[l] != val:
                l += 1

            while l < h and nums[h] == val:
                h -= 1

            if l < h:
                nums[l],nums[h] = nums[h],nums[l]
        return l + 1 if nums[l] != val else l



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        pass
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
