# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import *
import unittest

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        new_head = ListNode(0)

        p = head

        while p:
            p_next = p.next
            q = new_head

            while q.next and q.next.val < p.val:
                q = q.next
            
            p.next = q.next
            q.next = p            

            p = p_next
        return new_head.next

class TestSortList(TestList):

    def test_sort(self):
        head = self.make_list([2,4,7,1,3,6])
        s = Solution()
        head = s.insertionSortList(head)
        self.traversal_list(head)


if __name__ == "__main__":
    unittest.main()