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
            if start == end:
                return TreeNode(nums[start])
            
            m = (start + end) // 2
            mid = TreeNode(nums[m])
            TreeNode

        if head is None:
            return head
        
        nums = []

        while head:
            nums.append(head.val)
        start = 0
        end = len(nums)
