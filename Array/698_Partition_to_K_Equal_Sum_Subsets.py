import unittest

class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) < k:
            return False

        buckets = [0] * k
        sum_ = sum(nums)
        nums.sort()
        if sum_ % k != 0:
            return False
        
        target = sum_ // k

        def helper(nums):
            if len(nums) == 0:
                for bucket in buckets:
                    if bucket != target:
                        return False
                return True
            
            for index,num in enumerate(nums):
                if index > 0 and nums[index] == nums[index-1]:
                    continue
                for j, bucket in enumerate(buckets):
                    if j > 0 and buckets[j] == buckets[j-1]:
                        continue
                    if bucket + num <= target:
                        buckets[j] += num
                        if helper(nums[:index]+nums[index+1:]):
                            return True
                        buckets[j] -= num
            return False
        return helper(nums)
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertTrue(self.s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    
    def test_two(self):
        self.assertTrue(self.s.canPartitionKSubsets(
            [10, 12, 1, 2, 10, 7, 5, 19, 13, 1], 4))

if __name__ == "__main__":
    unittest.main()
