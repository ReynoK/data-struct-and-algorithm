import unittest

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []

        nums.sort()
        solutions = []

        for index in range(0, len(nums) - 2):
            if index > 0 and nums[index] == nums[index-1]:
                continue

            p = index + 1
            q = len(nums) -1 

            while p < q:
                sum_ = nums[p] + nums[q] + nums[index]

                if sum_ > 0:
                    q -= 1
                elif sum_ < 0:
                    p += 1
                else:
                    solutions.append([nums[index], nums[p], nums[q]])
                    
        return solutions

class TestSolution(unittest.TestCase):
    def test_one(self):
        input = [-1, 0, 1, 2, -1, -4]
        s = Solution()
        print(s.threeSum(input))


if __name__ == "__main__":
    unittest.main()