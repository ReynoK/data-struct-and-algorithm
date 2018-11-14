import unittest

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = sum(nums[:3])

        for index in range(len(nums)-2):
            p = index + 1
            q = len(nums) - 1

            temp_target = target - nums[index]

            # 优化
            sum_ = sum(nums[index:index+3])
            if sum_ > target:
                if abs(target - sum_) < abs(target-closest_sum):
                    closest_sum = sum_
                continue
            sum_ = sum([nums[index]] + nums[-2:])
            if sum_ < target:
                if abs(target - sum_) < abs(target-closest_sum):
                    closest_sum = sum_
                continue

            while p < q:
                sum_ = nums[p] + nums[q]
                if abs(temp_target - sum_) < abs(target-closest_sum):
                    closest_sum = nums[index] + nums[p] + nums[q]

                if sum_ == temp_target:
                    return target
                elif sum_ < temp_target:
                    p += 1
                else:
                    q -= 1

        return closest_sum
        
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [-1, 2, 1, -4]
        self.assertEqual(self.s.threeSumClosest(input, 1), 2)
    
    def test_two(self):
        input = [-1, 2, 1, -4]
        self.assertEqual(self.s.threeSumClosest(input, 1), 2)

if __name__ == "__main__":
    unittest.main()
