import unittest


class Solution:
    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h)//2

            if nums[m] == target:
                return True

            if target > nums[m]:
                if nums[m] > nums[l]:
                    l += m
                elif nums[m] == nums[l]:
                    l += 1
                else:
                    # 右边有序
                    if target > nums[h]:
                        h = m - 1
                    else:
                        l = m + 1
            else:
                if nums[m] < nums[h]:
                    # 右边有序
                    h = m - 1
                elif nums[m] == nums[h]:
                    h = h - 1
                else:
                    # 左边有序
                    if target < nums[l]:
                        l = m + 1
                    else:
                        h = m - 1
        return False

    def search(self, nums, target):
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2

            if nums[m] == target:
                return True
            
            if nums[m] == nums[l] and nums[m] == nums[h]:
                # 如果前后中都相等，那么大多数数字都是该值，转化为顺序查找
                for n in nums:
                    if n == target:
                        return True
                return False
            
            # 两种情况
            # ①左边有序
            if nums[m] >= nums[l]:
                #如果位于左区间
                if target>=nums[l] and target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            # 如果右边有序
            else:
                # 位于右区间
                if target > nums[m] and target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
        
        return False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [2, 5, 6, 0, 0, 1, 2]
        self.assertTrue(self.s.search(input, 0))
    
    def test_two(self):
        input = [2, 5, 6, 0, 0, 1, 2]
        self.assertTrue(self.s.search(input, 3))

if __name__ == "__main__":
    unittest.main()
