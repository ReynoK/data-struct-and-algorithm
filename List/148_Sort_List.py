"""
链表排序：
思路：首先计算长度，然后通过长度来使用归并排序
注意点：注意指针的位移
"""


from utils import *
import unittest

class Solution(object):
    def merger(self, l1, l2):
        """合并有序链表
        """

        fake_head = ListNode(0)
        p = fake_head

        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next                      # 不要忘记位移
        p.next = l1 if l1 else l2
        return fake_head.next
        

    def sort(self, head, len):
        if len == 1:
            return head
        
        l = len//2
        r = len - l
        p = head
        move = l
        while move > 1:
            p = p.next
            move -= 1
        q = p.next
        p.next = None
        
        left_list = self.sort(head, l)
        right_list = self.sort(q, r)

        return self.merger(left_list, right_list)


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        n = 0
        p = head 

        while p:
            n += 1
            p = p.next
        return self.sort(head, n)

class TestSortList(TestList):
    def test_sort_list(self):
        head = self.make_list([3,2,4,5,1,8,7])
        s = Solution()
        head = s.sortList(head)
        self.traversal_list(head)

    # def test_merger(self):
    #     head1 = self.make_list(["1","3","5"])
    #     head2 = self.make_list(["2","4","6"])
    #     s = Solution()
    #     head = s.merger(head1, head2)
    #     self.traversal_list(head)

if __name__ == "__main__":
    unittest.main()