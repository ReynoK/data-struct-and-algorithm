import unittest


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None

        max_group = [None, None, None]

        for num in nums:
            if num in max_group:
                continue
            else:
                if max_group[0] is None or max_group[0]<num:
                    max_group[0],max_group[1],max_group[2] = num,max_group[0],max_group[1]
                elif max_group[1] is None or max_group[1] < num:
                    max_group[1],max_group[2] = num, max_group[1]
                elif max_group[2] is None or max_group[2] < num:
                    max_group[2] = num
        return max_group[-1] if max_group[-1] is not None else max_group[0]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [3, 2, 1]
        self.assertEqual(self.s.thirdMax(input), 1)
    
    def test_two(self):
        input = [3,2]
        self.assertEqual(self.s.thirdMax(input), 3)

if __name__ == "__main__":
    unittest.main()
