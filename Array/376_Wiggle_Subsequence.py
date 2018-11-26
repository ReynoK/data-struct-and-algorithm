import unittest


class Solution:
    def wiggleMaxLength(self, nums):
        length = len(nums)

        if length < 1:
            return 0

        

    def wiggleMaxLength2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)

        if length < 1:
            return 0

        dp = [[0]*length for _ in range(2)]
        dp[0][0] = dp[1][0] = 1

        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[0][i] = max(dp[0][i], dp[1][j]+1)
                elif nums[i] < nums[j]:
                    dp[1][i] = max(dp[1][i], dp[0][j] + 1)
        return max(max(dp[0]), max(dp[1]))

        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.wiggleMaxLength([1, 7, 4, 9, 2, 5]), 6)
    
    def test_two(self):
        self.assertEqual(self.s.wiggleMaxLength(
            [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]), 7)

    def test_three(self):
        self.assertEqual(self.s.wiggleMaxLength(
            [1, 2, 3, 4, 5, 6, 7, 8, 9]), 2)

if __name__ == "__main__":
    unittest.main()
