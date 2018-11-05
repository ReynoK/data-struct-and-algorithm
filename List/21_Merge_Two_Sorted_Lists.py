"""合并有序链表
思路：创建一个表头，用来执行合并后的链表，然后判断l1和l2链表头的值直到其中一方已经到达尾部，
然后将还有值的链表添加到尾部。
注意点：新链表，也需要一个指针，指向尾部
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p = head

        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next          # 位移指针
        
        if l1:
            p.next = l1
        else:
            p.next = l2

        return head.next
