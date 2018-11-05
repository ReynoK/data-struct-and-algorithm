"""
寻找链表的中间节点，如果中间节点为偶数个，那么就返回第二个

思路：用两个指针，第一个指针前进一步，第二个指针前进两步，当第二个指针到达终点时，
第一个指针指向的值，即为中心点，因为偶数个要返回第二个，因此先第二个指针第一次移动时，
如果刚好到达尾部，表示该链表为奇数个，如果只能再走一步，该链表个数为偶数个，因此按第二个
指针移动一次，第一个指针移动一次，第二个指针移动一次，这样循环，就可以符合题目要求。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p,q = head,head

        while True:
            if q.next is None:
                return p
            q = q.next
            p = p.next

            if q.next is None:
                return p
            q = q.next