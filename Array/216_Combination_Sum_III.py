import unittest

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        result = []

        def helper(k, n, start, solution):
            if n < 0:
                return
            if k == 0:
                if n == 0:
                    result.append(solution)
                else:
                    return 
            for num in range(start, 10):
                tmp = solution.copy()
                tmp.append(num)
                helper(k-1, n-num,num + 1, tmp)

        helper(k,n,1,[])
        return result


class TestComninationSum(unittest.TestCase):
    def test_one(self):
        s = Solution()
        print(s.combinationSum3(3,9))

if __name__ == "__main__":
    unittest.main()