import unittest


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        p = 0 
        q = len(height) - 1

        max_area = 0 

        while p < q:
            area = 0

            if height[p] < height[q]:
                area = height[p] * (q-p)
                p += 1
            else:
                area = height[q] * (q-p)
                q -= 1
            max_area = max(max_area, area)

        return max_area


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.s.maxArea(input), 49)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
