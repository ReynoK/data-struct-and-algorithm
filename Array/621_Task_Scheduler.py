import unittest

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        bucket = {}

        for task in tasks:
            if task not in bucket:
                bucket[task] = 1
            else:
                bucket[task] += 1

        interval = 0
        while True:
            print(bucket)
            per_iterval = 0
            for key,value in bucket.items():
                if value > 0:
                    per_iterval += 1
                    bucket[key] -= 1
            if per_iterval == 0:
                break
            interval = interval + per_iterval + per_iterval
        return interval if interval == 0 else interval - n


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_one(self):
        input = ["A", "A", "A", "B", "B", "B"]
        self.assertEqual(self.s.leastInterval(input,2 ), 8)


if __name__ == "__main__":
    unittest.main()
