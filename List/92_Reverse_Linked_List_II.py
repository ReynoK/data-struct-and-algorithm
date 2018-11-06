"""
反转链表中的某一段，要求一次遍历
思路：寻找开始反转节点的前一个节点，然后开始反转后续节点，需要操作 n-m次，少一次的原因是开始节点不用回转

注意点：结束变量的设置

"""

from utils import *
import unittest

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if head is None:
            return None
        
        fake_head = ListNode(0)
        fake_head.next = head

        p = fake_head
        t = m               # 设置一个临时变量来存储m
        while t - 1 > 0:
            p = p.next
            t -= 1          # 注意更新条件变量
        
        times = n - m       # 注意截止条件
        q = p.next
        while times > 0:
            r = q.next
            q.next = r.next
            r.next = p.next
            p.next = r

            times -= 1
        return fake_head.next

class TestReverseBetween(TestList):
    def test_reverse_haed_begin(self):
        head = self.make_list([1,2,3,4,5])
        s = Solution()
        head = s.reverseBetween(head, 1,3)
        self.traversal_list(head)

    def test_reverse_haed(self):
        head = self.make_list([1, 2, 3, 4, 5])
        s = Solution()
        head = s.reverseBetween(head, 2, 4)
        self.traversal_list(head)


if __name__ == "__main__":
    unittest.main()
