import unittest


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        if len(S) == 0:
            return []

        start_index = 0
        group_alp = S[0]
        result = []

        for index,s in enumerate(S):    
            if s != group_alp:
                if index - start_index >= 3:
                    result.append([start_index, index-1])
                start_index = index
                group_alp = s

        if index - start_index + 1 >= 3:
            result.append([start_index, index])

        return result
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = "abbxxxxzzy"
        self.assertEqual(self.s.largeGroupPositions(input), [[3, 6]])
    
    def test_two(self):
        input = "abc"
        self.assertEqual(self.s.largeGroupPositions(input), [])

    def test_three(self):
        input = "abcdddeeeeaabbbcd"
        self.assertEqual(self.s.largeGroupPositions(
            input), [[3, 5], [6, 9], [12, 14]])

if __name__ == "__main__":
    unittest.main()
