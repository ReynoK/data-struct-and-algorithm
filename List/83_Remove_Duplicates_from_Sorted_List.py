"""删除链表中的重复元素
思路：前后指针，比较前后指针的值是否一致，不一致则要往前跳，若之前有重复，还要更新next，
最后一步，要更新next值，因为如果最后一个是重复的值，如果不更新，则最后一对数据不会去重，因为直接跳出了
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        p = head
        q = head.next

        while q:
            if q.val == p.val:
                q = q.next
            else:
                p.next = q
                p = q
                q = q.next
        p.next = q
        return head