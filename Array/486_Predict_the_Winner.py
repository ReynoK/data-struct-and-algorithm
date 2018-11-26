import unittest


class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)

        cache = {}

        def helper(i,j):
            if i > j:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            round = length - (j - i + 1)

            if round%2 == 0:
                # player 1 round 
                cache[(i, j)] = max(helper(i+1, j) + nums[i], helper(i, j-1) + nums[j])
            else:
                cache[(i, j)] = min(helper(i+1, j) - nums[i], helper(i, j-1) - nums[j])

            return cache[(i, j)]

        return helper(0, length-1)>=0

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1, 5, 2]
        self.assertFalse(self.s.PredictTheWinner(input))
    
    def test_two(self):
        input = [1, 5, 233, 7]
        self.assertTrue(self.s.PredictTheWinner(input))

if __name__ == "__main__":
    unittest.main()
