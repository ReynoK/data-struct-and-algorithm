import unittest


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.sum_coll = [0]

        for num in nums:
            self.sum_coll.append(self.sum_coll[-1] + num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.sum_coll[j+1] - self.sum_coll[i] 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        pass
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
