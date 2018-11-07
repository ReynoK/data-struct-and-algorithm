from utils import *
import unittest

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        p = root
        cnt = 0
        result = []
        while p:
            cnt += 1
            p = p.next
        
        assign_num = []
        if cnt < k:
            assign_num = [1]*cnt + [0]*(k - cnt)
        else:
            assign_num = [cnt//k + 1]*(cnt%k) + [cnt//k]*(k - cnt%k)

        p = root
        print(assign_num)
        for num in assign_num:
            if num == 0:
                result.append(None)
            else:
                r = p
                while num > 1:
                    r = r.next
                    num -= 1

                result.append(p)
                p = r.next
                r.next = None
        return result                

class TestSplitList(TestList):
    def test_k_less_length(self):
        head = self.make_list([1,2,3,4,5])
        s = Solution()
        heads = s.splitListToParts(head, 3)

        for head in heads:
            self.traversal_list(head)

    def test_k_greater_length(self):
        head = self.make_list([1, 2, 3, 4, 5])
        s = Solution()
        heads = s.splitListToParts(head, 10)

        for head in heads:
            self.traversal_list(head)


if __name__ == "__main__":
    unittest.main()
