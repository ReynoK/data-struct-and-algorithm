import unittest


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        result = [0] * len(triangle)
        result[0] = triangle[0][0]
        last = 0
        for i in range(1, len(triangle)):
            last = result[0]
            for j in range(0, i + 1):
                if j == 0:
                    last = result[0]
                    result[0] += triangle[i][0]
                elif j == i:
                    result[j] = last + triangle[i][j]
                else:
                    temp = result[j]
                    result[j] = triangle[i][j] + min(last, result[j])
                    last = temp
        return min(result)



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]

        self.assertEqual(self.s.minimumTotal(input), 11)

    def test_two(self):
        pass


if __name__ == "__main__":
    unittest.main()
