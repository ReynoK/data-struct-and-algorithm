# 从链表中删除元素
# 该出的只有要被删除节点的位置，因此就是要把后面节点的值往前移动，
# 那么，关键点就在于最后一步的时候要怎么离开循环。
# 重点：每一步要现赋值在判断是否返回，否则最后一步会导致值没有向前移动

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        p = node
        q = p.next

        while q:
            p.val = q.val

            if q.next is None:
                p.next = None
                return 
            p = q
            q = q.next

            
