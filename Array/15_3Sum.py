import unittest

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        length = len(nums)
        result = []

        for index in range(0,length - 2):
            if index > 0 and nums[index] == nums[index-1]:
                continue
        
            target = -nums[index]
            p = index + 1
            q = length - 1

            while p < q:
                sum_ = nums[p] + nums[q]
                if sum_ == target:
                    result.append([nums[index], nums[p], nums[q]])
                    p += 1
                    while p < q and (nums[p] == nums[p - 1]):
                        p += 1
                elif sum_ > target:
                    q -=1 
                else:
                    p += 1
        return result

class TestSolution(unittest.TestCase):
    def test_one(self):
        input = [-1, 0, 1, 2, -1, -4]
        s = Solution()
        print(s.threeSum(input))

    def test_two(self):
        input = [0,0,0]
        s = Solution()
        print(s.threeSum(input))


if __name__ == "__main__":
    unittest.main()
