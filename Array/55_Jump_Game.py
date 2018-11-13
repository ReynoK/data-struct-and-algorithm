import unittest

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) == 0 or nums[0] == 0:
            return False

        p = len(nums) -1 

        while p > 0:
            if nums[p] != 0:
                p -= 1
                continue
            else:
                q = p - 1
                while q >= 0 and nums[q] + q <= p:
                    q -= 1
                
                if q == -1:
                    return False

                p = q - 1

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [2, 3, 1, 1, 4]
        self.assertTrue(self.s.canJump(input))

    def test_two(self):
        input = [3, 2, 1, 0, 4]
        self.assertFalse(self.s.canJump(input))

if __name__ == "__main__":
    unittest.main()