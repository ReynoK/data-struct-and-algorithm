# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return [[]]

        result = []

        node_list = [root]

        while node_list:
            tmp_node_list = []
            rows = []
            for node in node_list:
                rows.append(node.val)

                if node.left:
                    tmp_node_list.append(node.left)
                if node.right:
                    tmp_node_list.append(node.right)
            result.append(rows)
            node_list = tmp_node_list

        return result
