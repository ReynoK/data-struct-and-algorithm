import unittest


class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
        pairs = sorted(pairs, lambda x:x[0])

        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [[1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.s.findLongestChain(input), 2)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
