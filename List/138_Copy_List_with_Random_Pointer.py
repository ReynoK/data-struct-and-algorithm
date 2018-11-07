# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        old_list = dict()
        new_list = list()

        p = head
        new_head = RandomListNode(0)
        q = new_head
        n = 1
        while p:
            old_list[n] = p
            new_node = RandomListNode(p.label)
            new_node.random = p.random
            new_list.append(new_node)
            q.next = new_node
            q = new_node
            p = p.next

        q = new_head.next
        while q:
            q.random = new_list[old_list[q.random]]

        return new_head.next
