class Solution(object):

    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increasing = True
        decreasing = True

        for num in range(1, len(A)):
            if A[num] == A[num-1]:
                continue
            elif A[num] > A[num-1]:
                decreasing = False
            else:
                increasing = False

            if not increasing and not decreasing:
                break

        return increasing or decreasing

        