import unittest

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        result = []

        plus = 1

        for index in range(len(digits) - 1, -1, -1):
            sum_ = digits[index] + plus

            if sum_ > 9:
                plus = 1
                sum_ %= 10
            else:
                plus = 0
            
            result.append(sum_)

        if plus:
            result.append(plus)
        
        return result[::-1]

class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [1,2,3]
        print(self.s.plusOne(input))

    def test_two(self):
        input = [9,9,9]
        print(self.s.plusOne(input))

if __name__ == "__main__":
    unittest.main()


