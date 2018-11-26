import unittest


class Solution:
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """

        dp = [1] * 4
        soups = [[N,N] for _ in range(4)]
        a_res = 0
        a_b_res = 0

        while True:
            dp_tmp =  [0]*4
            not_a_soup = True
            for soup in soups:
                if soup[0] > 0:
                    not_a_soup = False
                    soup[]

            
            if not_a_soup:
                break

        return res
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.soupServings(50), 0.625)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
