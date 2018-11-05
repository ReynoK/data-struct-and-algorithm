"""反转链表
①：制造一个假头部，然后不断在假头部和下一个节点之间不断插入新数据
②：不断遍历链表元素，将元素移动到链表开头

"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        fake_head = ListNode()

        while head:
            next = head.next
            head.next = fake_head.next
            fake_head.next = head
            head = next


        return fake_head.next

    def reverseList2(self, head):

        if head is None:
            return None
        
        pre = head

        while True:
            cur = pre.next
            if cur is None:
                return head

            pre.next = cur.next
            cur.next = head
            head = cur