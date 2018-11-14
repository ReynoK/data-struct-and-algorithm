class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        cache = {}
        def helper(m,n):
            if (m,n) in cache:
                return cache[(m,n)]

            if m == 1 or n == 1:
                return 1

            cache[(m, n)] = helper(m-1, n) + helper(m, n-1)
            return cache[(m,n)]

        return helper(m,n)
