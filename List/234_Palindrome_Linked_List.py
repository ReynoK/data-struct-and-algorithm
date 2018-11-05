"""看链表是否是回数
思路1：简单，遍历列表，将列表存到list中，然后判断 list == list[::-1]
思路2：找到链表中点，如果是偶数节点，则找到中间节点的第一个节点（画图好理解，判断条件为q.next is None or q.next.next is None），
然后反转后续列表，然后用两个指针，第一个指针指向头节点，第二个节点指向后半节点开头，比较数是否相等。比较的次数为后半节点的节点数量。
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return False

        if head.next is None:
            return True
        
        p = head
        q = head

        while True:
            if q.next is None or q.next.next is None:
                break

            q = q.next.next
            p = p.next

        q = p.next
        # 反转后续列表
        r = q.next

        while r:
            q.next = r.next
            r.next = p.next
            p.next = r
            r = q.next

        #开始比较
        q = p.next
        p = head

        while q:
            if p.val != q.val:
                return False
            
            p = p.next
            q = q.next

        return True
        