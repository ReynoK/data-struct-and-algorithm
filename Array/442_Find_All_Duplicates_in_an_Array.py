import unittest

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        for num in nums:
            index = abs(num)

            if nums[index-1] > 0:
                nums[index-1] = -nums[index-1]
            elif nums[index-1] < 0:
                result.append(index)

        return result


class TestSolution(unittest.TestCase):
    def test_one(self):
        input = [4, 3, 2, 7, 8, 2, 3, 1]
        s = Solution()
        print(s.findDuplicates(input))

if __name__ == "__main__":
    unittest.main()
