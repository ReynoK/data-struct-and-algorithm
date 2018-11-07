"""链表每k个旋转
思路：先计算总体长度，然后按k计算有几个组需要旋转，然后找到每个要旋转的组的前一个节点

Returns:
    [type] -- [description]
"""



from utils import *
import unittest

class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        fake_head = ListNode(0)
        fake_head.next = head

        cnt = 0
        p = fake_head
        while p.next:
            cnt += 1
            p = p.next

        times = cnt // k

        p = fake_head
        
        while times > 0:
            i = 1
            q = p.next
            while i < k:
                r = q.next
                q.next = r.next
                r.next = p.next
                p.next = r
                i += 1
            p = q               # 下一个旋转的前节点
            times -= 1
        return fake_head.next

class TestReverseList(TestList):
    def test_one(self):
        head = self.make_list([1,2,3,4,5])
        s = Solution()
        head = s.reverseKGroup(head, 3)
        self.traversal_list(head)

if __name__ == "__main__":
    unittest.main()





