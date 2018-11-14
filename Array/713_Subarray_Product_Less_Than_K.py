import unittest

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        count = 0
        product = 1
        p = q = 0

        while q < len(nums):
            product *= nums[q]
            
            while p <= q and product >= k:
                product /= nums[p]
                p += 1
            
            if product < k :
                count += (q - p + 1)
            q += 1

        return count
    
class TestSolution(unittest.TestCase):
    def test_one(self):
        input = [10, 5, 2, 6]
        s = Solution()
        print(s.numSubarrayProductLessThanK(input, 100))

    def test_two(self):
        input = [1,2,3]
        s = Solution()
        print(s.numSubarrayProductLessThanK(input,0) )

if __name__ == "__main__":
    unittest.main()
