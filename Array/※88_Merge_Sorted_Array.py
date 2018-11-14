"""将有序数组1和2合并，并放到数组1中，保持有序

Returns:
    [type] -- [description]
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        insert_position = len(nums1) - 1

        p1 = m-1
        p2 = n-1

        while p1>=0 and p2>=0:
            if nums1[p1] >= nums2[p2]:
                nums1[insert_position] = nums1[p1]
                p1 -= 1
                insert_position -= 1
            else:
                nums1[insert_position] = nums2[p2]
                p2 -= 1
                insert_position -= 1

        while p1>=0:
            nums1[insert_position] = nums1[p1]
            p1 -= 1
            insert_position -= 1

        while p2>=0:
            nums1[insert_position] = nums2[p2]
            p2 -= 1
            insert_position -= 1

        return 

    def merge2(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
