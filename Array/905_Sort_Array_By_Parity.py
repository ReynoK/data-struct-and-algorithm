"""变更数组，使得偶数在前半部分，奇数后半部分

Returns:
    [type] -- [description]
"""


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        odd_list = []
        even_list = []

        for num in A:
            if num%2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)

        return even_list + odd_list