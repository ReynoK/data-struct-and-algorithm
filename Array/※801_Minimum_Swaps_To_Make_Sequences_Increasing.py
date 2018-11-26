import unittest

"""数组长度相等的A和B，求最少交换A[i]和B[i]使得A和B都严格有序

思路：因为结果能够保证A和B交换后严格有序因此,A[i]和B[i]必须满足(A[i]>A[i-1] B[i]>B[i-1])或者（A[i]>B[i-1] B[i]>A[i-1]）必须至少满足一个，否则无法形成严格有序。
因此A[i]/B[i]为结尾的子数组，取决于A[i-1]/B[i-1]的结果。如果 A[i]>A[i-1] B[i]>B[i-1]，那么B[i-1]/A[i-1]交换，那么A[i]/B[i]也要跟着换。同理，如果A[i]>B[i-1] B[i]>A[i-1]，
，那么B[i-1]/A[i-1]交换，那么A[i]/B[i]无需换，否则，需要换。
"""


class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        length = len(A)

        n1, s1 = 0, 1
        if length == 0:
            return 0

        for i in range(1, length):
            n2 = s2 = float('inf')
            if A[i] > A[i-1] and B[i] > B[i-1]:
                n2 = min(n2, n1)
                s2 = min(s2, s1+1)
            
            if A[i] > B[i-1] and B[i] > A[i-1]:
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)

            n1,s1 = n2,s2
        return min(s1,n1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.minSwap([1, 3, 5, 4], [1, 2, 3, 7]), 1)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
