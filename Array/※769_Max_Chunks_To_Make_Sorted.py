import unittest

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        right_min = [-1]*len(arr)
        min_num = len(arr) + 1
        for index in range(len(arr)-1, -1, -1):
            if arr[index] < min_num:
                min_num = arr[index]
            
            right_min[index] = min_num
        print(right_min)
        count = 1
        for index in range(1, len(right_min)):
            if right_min[index] != right_min[index-1]:
                count += 1
        return count

class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        input = [3,2,1,5,4,6]
        self.assertEqual(s.maxChunksToSorted(input), 3)

    def test_two(self):
        s = Solution()
        input = [4, 3, 2, 1, 0]
        self.assertEqual(s.maxChunksToSorted(input), 1)

    def test_three(self):
        s = Solution()
        input = [2,0,1]
        self.assertEqual(s.maxChunksToSorted(input), 1)

if __name__ == "__main__":
    unittest.main()
