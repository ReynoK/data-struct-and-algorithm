"""
flatten“多维”链表

思路：递归flatten，注意把控好终止条件，和指针的操作
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def helper(self, head):
        """该函数返回头尾，提高速度
        
        Arguments:
            object {[type]} -- [description]
            head {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """

        if head is None:
            return head

        p = head
        tail = p
        while p:
            tail = p
            if p.child is None:
                p = p.next
            else:
                q = p.next
                child_head,child_tail = self.helper(p.child)            
                p.child = None
                
                p.next = child_head
                child_head.prev = p
                child_tail.next = q
                tail = child_tail           # 这边要改变tail的值
                if q:                       # 有可能在当前链表的最后一个节点进行flatten，因此要判断下一个节点的q是不是为None
                    q.prev = child_tail
                p = q

        return head,tail

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if head is None:
            return head

        return self.helper(head)[0]

        
