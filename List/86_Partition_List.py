from utils import *
import unittest

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if head is None:
            return None

        less_head = ListNode(0)
        greater_equal_head = ListNode(0)

        p = head
        q = less_head
        r = greater_equal_head

        while p:
            if p.val < x:
                q.next = p
                q = q.next
            else:
                r.next = p
                r = r.next
            p = p.next

        r.next = None
        q.next = greater_equal_head.next
        return less_head.next

class TestPartition(TestList):
    def test_partition(self):
        head = self.make_list([1,3,5,7,9,2,4,6,8])
        s = Solution()
        head = s.partition(head, 5)
        self.traversal_list(head)

if __name__ == "__main__":
    unittest.main()
    
                