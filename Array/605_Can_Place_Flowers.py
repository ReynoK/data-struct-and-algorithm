import unittest

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1:
            can_paint = 1 if flowerbed[0] == 0 else 0
            return can_paint >= n

        can_paint = 0
        start = 0
        while start < len(flowerbed) and flowerbed[start] == 0:
            start += 1

        can_paint += start//2

        for index in range(start,len(flowerbed)):
            if flowerbed[index] == 1:
                distance = index - start - 1
                if distance > 0:
                    can_paint += (distance-1) // 2
                start = index
        if start < len(flowerbed):
            can_paint += (len(flowerbed) - start - 1)//2

        return can_paint >= n

class TestCanPlace(unittest.TestCase):
    def test_one(self):
        s = Solution()
        nums = [1, 0, 0, 0, 0, 1]
        print(s.canPlaceFlowers(nums,2))

if __name__ == "__main__":
    unittest.main()


