import unittest


class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        hash_coll = defaultdict(lambda:0)
        count = 0

        if k < 0:
            return count

        for num in nums:
            hash_coll[num] += 1

        for num in hash_coll.keys():
            if hash_coll[num] == 0:
                continue

            if k == 0: 
                if hash_coll[num] > 1:
                    count += 1
                continue
            
            another = num - k
            if another in hash_coll:
                hash_coll[another] = 0
                count += 1

            another = num + k
            if another in hash_coll:
                hash_coll[another] = 0
                count += 1

        return count
                


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = [3, 1, 4, 1, 5]
        self.assertEqual(self.s.findPairs(input, 2), 2)
    
    def test_two(self):
        input = [1, 3, 1, 5, 4]
        self.assertEqual(self.s.findPairs(input, 0 ), 1)

if __name__ == "__main__":
    unittest.main()
