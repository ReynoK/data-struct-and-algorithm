import unittest

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        
        result = [0] * (rowIndex + 1)
        result[0] = 1
        for i in range(2, rowIndex+2):              # 要算好层次的数量
            last = 0
            for j in range(i):
                temp = result[j]
                result[j] = result[j] + last
                last = temp

            print(result)

        return result




class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.getRow(3), [1,3,3,1])
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
