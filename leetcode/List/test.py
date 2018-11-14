# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root.left is None and root.right is None:
            return 0

        if root.left is None:
            return 1 + self.minDepth(self.right)
        elif root.right is None:
            return self.minDepth(self.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))