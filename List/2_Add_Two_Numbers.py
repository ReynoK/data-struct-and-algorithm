"""使用链表来表示数字的和
思路：因为和计算是从低位算起的，因此先反转链表，从低位算起，往前进位，不足的位数用0补齐，最后还要判断是否要多增加一个进位，最后再反转列表
注意点：
1. 0位补齐
2. 需要判断是否需要进位
3. 是否要生成一个最高位

Returns:
    [type] -- [description]
"""


# Definition for singly-linked list.
import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        new_head = ListNode(0)
        p = new_head

        save_flag = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + save_flag

            save_flag = 0

            if value > 9:
                save_flag = 1
            new_node = ListNode(value % 10)
            p.next = new_node
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if save_flag == 1:
            p.next = ListNode(1)

        return new_head.next


class TestList(unittest.TestCase):
    def make_list(self, nums):
        fake_head = ListNode(0)

        p = fake_head
        for num in nums:
            temp = ListNode(num)
            p.next = temp
            p = p.next
        return fake_head.next

    def traversal_list(self, head):
        while head:
            print(head.val, sep=' ', end='')
            head = head.next
        print("")

    def test_logical(self):
        head1 = self.make_list([1, 2, 3, 4, 5])
        head2 = self.make_list([6, 7, 8, 9])
        s = Solution()
        head = s.addTwoNumbers(head1, head2)
        self.traversal_list(head)
        # print(head.val)


if __name__ == "__main__":
    unittest.main()
