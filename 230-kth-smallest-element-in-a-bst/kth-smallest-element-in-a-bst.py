# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        arr=[]

        def dfs(node):
            if not node:
                return None
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        arr.sort()
        return arr[k-1]
        