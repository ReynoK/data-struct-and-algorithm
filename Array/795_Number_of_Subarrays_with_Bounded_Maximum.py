import unittest


class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """

        if len(A) == 0:
            return 0

        compare = [0] * len(A)

        for index,num in enumerate(A):
            if num < L:
                compare[index] = -1
            elif num > R:
                compare[index] = 1

        def helper():
            pass

        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        pass
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
