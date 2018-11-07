"""旋转链表

思路：计算长度，取余，寻找开头，链接，即可
"""


from utils import *
import unittest

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None:
            return None

        len = 0
        p = head 
        while p:
            p = p.next
            len += 1

        k = k%len
        if k == 0:
            return head

        left = len - k
        p = head

        while left > 1:
            p = p.next
            left -= 1

        q = p.next
        p.next = None
        r = q

        while r.next:
            r = r.next
        
        r.next = head
        return q
class TestRotateList(TestList):
    def test_rotate_list(self):
        head = self.make_list([1,2,3,4,5])
        s = Solution()
        head = s.rotateRight(head, 5)
        self.traversal_list(head)


if __name__ == "__main__":
    unittest.main()
