import unittest

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length < 2:
            return length

        result = [0] * len(nums)
        result[0] = 1
        max_len = 0

        for i in range(1, length):
            temp = 0
            for j in range(0,i):
                if nums[i] > nums[j]:
                    temp = max(temp, result[j])
            result[i] = temp + 1
            max_len = max(max_len, result[i])

        return max_len

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(self.s.lengthOfLIS(input), 4)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
