"""检测循环的起点

Returns:
    [type] -- [description]
"""

from utils import *
import unittest

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        p = head
        q = head

        while True:
            if p.next and p.next.next:
                p = p.next.next
            else:
                return None
            q = q.next

            if p == q:
                break
        #计算圆圈长度

        n = 1
        p = q.next
        while p != q:
            n+=1 
            p = p.next
        # 向前走n步
        fake_head = ListNode(0)
        fake_head.next = head

        p = q = fake_head
        while n > 0:
            q = q.next
            n -= 1

        while p!=q:
            p = p.next
            q = q.next
        return p


class TestCycleList(TestList):
    def test_cycle(self):
        list_list = []
        p = head = ListNode(0)
        list_list.append(p)
        for i in range(1, 5):
            temp = ListNode(i)
            list_list.append(temp)
            p.next = temp
            p = p.next
        p.next = list_list[4]

        s = Solution()
        node = s.detectCycle(head)
        print(node.val)

if __name__ == "__main__":
    unittest.main()


        




        