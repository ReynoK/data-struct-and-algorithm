# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        head_ptr = ListNode(0)
        head_ptr.next = head

        p = q = head_ptr

        while n > 0:
            q = q.next
            n -= 1

        while q.next:
            q = q.next
            p = p.next

        p.next = p.next.next

        return head_ptr.next
