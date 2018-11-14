import unittest

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(candidates) == 0:
            return []

        solutions = []
        candidates.sort()

        def helper(target, candidates, solution):

            if target == 0:
                solutions.append(solution)
                return    

            if target < candidates[0]:
                return

            for index,_ in enumerate(candidates):
                tmp = solution[:]
                tmp.append(candidates[index])
                helper(target-candidates[index], candidates[index:], tmp)

        helper(target, candidates, [])
        return solutions


class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        print(s.combinationSum([2, 3, 5],8))


if __name__ == "__main__":
    unittest.main()
            

        
