"""删除链表内指定元素的值
 思路：需要记录前一个节点的位置，
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        fake_head = ListNode(0)

        fake_head.next = head
        p,q = fake_head,head

        while q:
            if q.val == val:
                q = q.next
            else:
                p.next = q
                p = q
                q = q.next
        p.next = q

        return fake_head.next

        
