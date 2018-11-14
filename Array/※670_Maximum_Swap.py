"""允许交换数字的两位，最多一次，找出变化后的最大数

思路：从低位到高位寻找其最右边最大的数（包括本身），然后在从高位看哪一位发生了其最右边的最大数不是本身，那么改位就是要交换的位，与其最右边最大的数进行交换

Returns:
    [type] -- [description]
"""


import unittest

class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        coll = []
        while num > 0:
            coll.append(num%10)
            num = num // 10 

        back = coll.copy()

        for i in range(1, len(back)):
            back[i] = max(back[i], back[i-1])

        index = len(coll) - 1

        while index >=0:
            if coll[index] == back[index]:
                index -= 1
                continue
            else:
                swap_index = coll.index(back[index])
                coll[index], coll[swap_index] = coll[swap_index], coll[index]
                break
        result = 0

        for index,num in enumerate(coll[::-1]):
            result *= 10
            result += num
        
        return result

class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        input = 2736
        self.assertEqual(s.maximumSwap(input), 7236)


    def test_two(self):
        s = Solution()
        input = 9973
        self.assertEqual(input, s.maximumSwap(input))


if __name__ == "__main__":
    unittest.main()
