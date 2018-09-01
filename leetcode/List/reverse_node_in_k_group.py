# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 寻找要反转链表的前面一个节点和后面一个节点（同时可以判断是否满足k个数量），然后反转这两个节点之间的链表 
# head_ptr   1  2  3  4  5  6  7   k = 6
#    ↑       ↑                 ↑
#    p       r                 q
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None:
            return head

        head_ptr = ListNode(0)
        head_ptr.next = head

        p = head_ptr
        q = head_ptr.next
        r = None
        while True:
            count = k
            can_end = False
            r = q
            while count > 0:
                # 循环 k 次，若不足k，则跳出
                if r is None:
                    can_end = True
                    break
                else:
                    r = r.next
                count -= 1
            
            if can_end:
                break
            
            while q.next != r:
                # 反转链表
                tmp = q.next
                q.next = q.next.next
                tmp.next = p.next
                p.next = tmp

            p = q
            q = q.next

        return head_ptr.next
