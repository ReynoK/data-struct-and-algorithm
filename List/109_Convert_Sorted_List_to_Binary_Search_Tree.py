"""有序链表转平衡二叉搜索树
思路：
1. 转换为数组，然后再转换为二叉搜索树，利用递归
2. 直接利用链表，找到每个链表的中间节点，在转换左右两边，利用递归
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def helper(nums, start,end):
            if start > end:
                return None
            elif start == end:
                return TreeNode(nums[start])
            
            m = (start + end) // 2
            mid = TreeNode(nums[m])
            mid.left = helper(nums, start, m-1)
            mid.right = helper(nums, m+1, end)
            
            return mid

        if head is None:
            return head
        
        nums = []

        while head:
            nums.append(head.val)
            head = head.next
        start = 0
        end = len(nums)

        return helper(nums, start, end-1)
