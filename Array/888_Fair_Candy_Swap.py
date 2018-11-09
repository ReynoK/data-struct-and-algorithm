class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        sum_a = sum(A)
        sum_b = sum(B)

        diff = abs(sum_a - sum_b)

        if sum_a > sum_b:
            set_a = set(A)
            for num in B:
                if num+diff in set_a:
                    return [num+diff, num]
        else:
            set_b = set(B)
            for num in A:
                if num+diff in set_b:
                    return [num, num+diff]
        