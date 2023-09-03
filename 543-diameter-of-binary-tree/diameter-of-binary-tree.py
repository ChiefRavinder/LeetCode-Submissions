# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDepth(root):
            if root is None:
                return 0
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        self.diameter = 0
        maxDepth(root)
        return self.diameter
