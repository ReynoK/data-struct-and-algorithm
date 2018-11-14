import unittest
import collections

class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counter = {v:k for k,v in enumerate(A)}
        result = collections.defaultdict(lambda:2)
        max_fib = 0

        for i in range(0, len(A)):
            for j in range(i+1, len(A)):
                a_k = A[j] - A[i]
                k = counter.get(a_k, None)
                if k is not None and k < i:
                    result[(j,i)] = result[(i,k)] + 1
                    max_fib = max(max_fib, result[(j,i)])

        return max_fib if max_fib >= 3 else 0

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    
    def test_one(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(self.s.lenLongestFibSubseq(input), 5)
    
    def test_two(self):
        input = [1, 3, 7, 11, 12, 14, 18]
        self.assertEqual(self.s.lenLongestFibSubseq(input), 3)

if __name__ == "__main__":
    unittest.main()
