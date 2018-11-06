"""删除链表中倒数第n个节点，最好一次遍历
思路：
①计算链表长度，然后计算要删除节点的位置，遍历2次
②两个指针，第二个指针前进n步，当后面节点的下一个节点是none，表示前一个节点是要被删除节点的前一个节点


注意点：头部节点的删除

Returns:
    [type] -- [description]
"""


import unittest
from utils import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 有可能删除头部节点
        fake_head = ListNode(0)
        fake_head.next = head
        p = q = fake_head

        while n >0:
            q = q.next
            n -= 1

        while True:
            if q.next is None:
                p.next = p.next.next
                break
            q = q.next
            p = p.next
        
        return fake_head.next

class TestRemoveNthNode(TestList):
    def test_remove_head(self):
        head = self.make_list([1,2,3,4,5])
        s = Solution()
        head = s.removeNthFromEnd(head, 5)
        self.traversal_list(head)

    def test_remove_mid(self):
        head = self.make_list([1,2,3,4,5])
        s = Solution()
        s.removeNthFromEnd(head, 2)
        self.traversal_list(head)

if __name__ == "__main__":
    unittest.main()
