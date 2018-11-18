import unittest


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return -1

        if nums[0] <= nums[-1]:
            return nums[0]

        l,h = 0,len(nums) - 1

        while l < h:
            m = l + (h-l)//2

            if nums[l] <= nums[m]:
                #左边有序
                if nums[m] <= nums[h]:
                    # 右边有序
                    return l
                else:
                    l = m+1
            else:
                #右边有序
                h = m
        return l


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [4,5,6,1,2,3]
        self.assertEqual(self.s.findMin(input), 3)
    
    def test_two(self):
        input = [1, 2, 3]
        self.assertEqual(self.s.findMin(input), 0)

if __name__ == "__main__":
    unittest.main()
