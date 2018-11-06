"""
每两个节点交换位置
思路:需要3个指针，分别指向前节点和待交换的两个节点

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import ListNode,TestList
import unittest

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head

        fake_head = ListNode(0)
        fake_head.next = head

        p,q,r = fake_head,head,head.next

        while q and r:
            p.next = r
            q.next = r.next
            r.next = q

            p = q
            q = p.next
            r = q.next if q else None
        
        return fake_head.next

class TestSwapPairs(TestList):
    def test_swap_pairs(self):
        head = self.make_list([1,2,3,4,5])
        s = Solution()
        head = s.swapPairs(head)
        self.traversal_list(head)

    def test_swap_pairs_even(self):
        head = self.make_list([1,2,3,4,5,6])
        s = Solution()
        head = s.swapPairs(head)
        self.traversal_list(head)


if __name__ == "__main__":
    unittest.main()