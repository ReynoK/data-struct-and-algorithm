import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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
