"""删除链表中所有的重复值节点
思路：需要两个指针，第一个指针之前的节点都是非重复节点，下一个指针在前一个指针之后，判断该指针的下一个指针的值是否与该值相等，
若相等，表示该元素为重复元素，向后删除元素直到尾节点或值不等于当前值；若不等，前一个指针往前移动，循环。

Returns:
    [type] -- [description]
"""


from utils import *
import unittest

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fake_head = ListNode(0)
        fake_head.next = head

        p = fake_head
        q = p.next

        while q:
            if q.next and q.next.val == q.val:
                value = q.val
                while q is not None and q.val == value:
                    q = q.next
                p.next = q
            else:
                p = p.next
                q = p.next
        return fake_head.next

class TestDeleteDuplicates(TestList):
    def test_one(self):
        head = self.make_list([1,2,2,2,3,4,5,5,6])
        s = Solution()
        head = s.deleteDuplicates(head)
        self.traversal_list(head)
    
    def test_null_list(self):
        head = None
        s = Solution()
        head = s.deleteDuplicates(head)
        self.traversal_list(head)

    def test_equal_list(self):
        head = self.make_list([1,1,1,1,1])
        s = Solution()
        head = s.deleteDuplicates(head)
        self.traversal_list(head)

if __name__ == "__main__":
    unittest.main()