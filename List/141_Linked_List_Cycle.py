# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        p,q= head,head.next

        while q:
            if p == q:
                return True
            q = q.next
            if not q:
                break
            q = q.next

            p = p.next
        
        return False