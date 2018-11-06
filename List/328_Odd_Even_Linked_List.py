"""分叉链表，前半部分为偶数位置节点，后半部分为奇数界定位置
思路：遍历列表，偶数节点、奇数节点分开，然后合并即可

Returns:
    [type] -- [description]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        odd_head = ListNode(0)
        even_head = ListNode(0)
        p = odd_head
        q = even_head
        odd_flag = True

        while head:
            if odd_flag:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next
            odd_flag = not odd_flag
        p.next = even_head.next
        q.next = None

        return odd_head.next
