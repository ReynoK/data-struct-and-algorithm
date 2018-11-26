import unittest


class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        counter = Counter(nums)

        avoid, using = 0,0
        prev = -1
        
        for num in sorted(counter):
            if num - 1 != prev:
                avoid, using = max(avoid, using), counter[num] * num + max(avoid, using)
            else:
                avoid, using = max(avoid, using), counter[num] * num + avoid
            prev = num

        return max(avoid, using)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [2, 2, 3, 3, 3, 4]
        self.assertEqual(self.s.deleteAndEarn(input), 9)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
