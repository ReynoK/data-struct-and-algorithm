"""计算新座位离最近同学的最大距离

思路：其实就是寻找连续0的中点，与前后1的距离，要注意坐在起点和终点时，计算方式的不同

Returns:
    [type] -- [description]
"""


import unittest

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        index = 0
        maxium_closest = 0

        while index < len(seats):
            if seats[index] == 0:
                start = index
                while index < len(seats) and seats[index] == 0:
                    index += 1
                if start == 0:
                    maxium_closest = max(maxium_closest, index)
                elif index == len(seats):
                    maxium_closest = max(maxium_closest, index - start)
                else:
                    maxium_closest = max(maxium_closest, index - (index+start)//2)
            else:
                index += 1
        return maxium_closest

class TestMaxDist(unittest.TestCase):
    def test_one(self):
        s = Solution()
        seats = [1,0,0,0,1,0,1]
        self.assertEqual(2, s.maxDistToClosest(seats))

    def test_two(self):
        s = Solution()
        seats = [0,0,0,0,0,1,0,0]
        self.assertEqual(5, s.maxDistToClosest(seats))

    def test_three(self):
        s = Solution()
        seats = [1,0,0,1,0,0,0,0,0]
        self.assertEqual(5,s.maxDistToClosest(seats))

if __name__ == "__main__":
    unittest.main()