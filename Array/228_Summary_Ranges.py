import unittest


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if len(nums) == 0:
            return []

        result = []
        start_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if i - 1 - start_index > 0:
                    result.append("{}->{}".format(nums[start_index], nums[i-1]))
                else:
                    result.append("{}".format(nums[start_index]))

                start_index = i
        
        if start_index < len(nums)-1:
            result.append("{}->{}".format(nums[start_index], nums[-1]))
        else:
            result.append("{}".format(nums[-1]))

        return result


class TestSolution(unittest.TestCase):
    def test_one(self):
        input = [0, 1, 2, 4, 5, 7]
        s = Solution()
        print(s.summaryRanges(input))


if __name__ == "__main__":
    unittest.main()
