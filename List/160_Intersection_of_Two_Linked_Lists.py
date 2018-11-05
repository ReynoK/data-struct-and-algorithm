"""寻找两个链表是否有交叉点
思路：先遍历两条链表的长度l1和l2，长的链表向前走|l1-l2|步，然后两条链表同时往前走，如果两条链表有相交，那么一定会在某个地方两个
节点指向同一元素

Returns:
    [type] -- [description]
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA is None or headB is None:
            return None

        l1 = 0
        l2 = 0

        p_a = headA
        while p_a:
            l1 += 1
            p_a = p_a.next
        p_b = headB
        while p_b:
            l2 += 1
            p_b = p_b.next

        if l1 > l2:
            diff = l1 - l2
            while diff > 0:
                headA = headA.next
                diff -= 1   
        else:
            diff = l2 - l1
            while diff > 0:
                headB = headB.next
                diff -= 1

        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None