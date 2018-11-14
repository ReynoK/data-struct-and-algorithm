import unittest

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        p0 = 0
        p1 = len(nums)-1

        index = 0

        while index <= p1:
            if nums[index] == 0:
                nums[index], nums[p0] = nums[p0], nums[index]       # 这时候 p0指向的位置只有为1
                p0+=1
            elif nums[index] == 2:
                nums[index],nums[p1] = nums[p1],nums[index]
                index -= 1
                p1 -= 1
            index += 1
        
class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        input = [2,0,2,1,1,0]
        s.sortColors(input)
        self.assertEqual([0,0,1,1,2,2], input)

    def test_two(self):
        s = Solution()
        input = [1,0,2]
        s.sortColors(input)
        self.assertEqual([0,1,2], input)

if __name__ == "__main__":
    unittest.main()
