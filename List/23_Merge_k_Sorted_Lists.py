"""合并K个有序链表

思路1：选择排序前每个链表第一个节点组成的，然后选在第一个元素插入新链表，第一个元素的下一个节点（非空）继续选择排序，如此循环
2. 改进版，使用堆排序提高速度
3. 两两合并俩表

Returns:
    [type] -- [description]
"""


from utils import *
import unittest

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if len(lists) == 0:
            return None
        fake_head = ListNode(0)

        p = fake_head
        lists = [x for x in lists if x is not None]         # 排除空链表

        lists = list(sorted(lists, key = lambda x:x.val))
        while lists:
            l = lists[0]
            p.next = l
            p = p.next
            l = l.next

            if l:
                lists[0] = l
                for index in range(1, len(lists)):
                    if lists[index].val < lists[index-1].val:
                        lists[index],lists[index-1] = lists[index-1],lists[index]
                    else:
                        break
            else:
                del lists[0]

        p.next = None
        return fake_head.next


class TestSortedList(TestList):
    def test_sort_test(self):
        lists = []
        lists.append(self.make_list([1,3,5,7,9]))
        lists.append(self.make_list([2,4,6,8]))
        lists.append(self.make_list([]))

        s = Solution()
        head = s.mergeKLists(lists)
        self.traversal_list(head)


if __name__ == "__main__":
    unittest.main()