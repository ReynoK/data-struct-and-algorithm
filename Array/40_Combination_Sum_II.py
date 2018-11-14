"""求和为target的子数组

思路：回溯法，candidates要变为有序，这样才能跳过重复解，并且可以直接跳过一些分支

Returns:
    [type] -- [description]
"""


import unittest

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        solutions = []
        candidates.sort()

        def helper(start, target, solution):
            if target == 0:
                solutions.append(solution)
                return 
            elif target < 0:
                return 
            
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index-1]:
                    continue

                #小优化
                if candidates[index] > target:
                    break
                helper(index+1,target-candidates[index], solution[:] + [candidates[index]])
        helper(0,target, [])
        return solutions

class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        input = [10, 1, 2, 7, 6, 1, 5]
        print(s.combinationSum2(input, 8))

if __name__ == "__main__":
    unittest.main()