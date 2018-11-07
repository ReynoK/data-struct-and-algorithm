"""按照要求重新排序列表，将后半部分的列表反转，间隔的插入到前半部分列表

思路：
1. 现将链表yifenweier；
2. 反转后半部分链表
3. 逐步插入

Returns:
    [type] -- [description]
"""


import unittest
from utils import *

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return 
        p = q = head

        while q.next and q.next.next:
            p = p.next
            q = q.next.next

        q = p.next
        p.next = None

        if q is None:
            return 

        #反转后半部分链表
        s = q
        r = q.next
        while r:
            s.next = r.next
            r.next = q
            q = r
            r = s.next
        p = head
        # 连接
        while q:
            q_next = q.next
            p_next = p.next
            q.next = p_next
            p.next = q
            p = p_next
            q = q_next

class TestReorderList(TestList):
    def test_reorder_list(self):
        head = self.make_list([])
        s = Solution()
        s.reorderList(head)
        self.traversal_list(head)


if __name__ == '__main__':
    unittest.main()





