import unittest


class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        cache = {}

        def helper(needs):
            res = 0
            for i in range(len(needs)):
                res += needs[i] * price[i]
            
            if res == 0:
                return 0

            if tuple(needs) in cache:
                return cache[tuple(needs)]

            for spe in special:
                temp_needs = needs[:]
                for index,need in enumerate(temp_needs):
                    if spe[index] > need:
                        break
                    temp_needs[index] -= spe[index]
                else:
                    res = min(res, helper(temp_needs) + spe[-1] )
            cache[tuple(needs)] = res

            return res
        
        return helper(needs)



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        self.assertEqual(self.s.shoppingOffers(
            [2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]), 11)
    
    def test_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
