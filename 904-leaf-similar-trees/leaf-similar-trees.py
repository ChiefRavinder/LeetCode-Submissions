# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        b1=[]
        b2=[]
        def DFS(root,s):
            if not root:
                return
            if root.right==None and root.left==None:
                s.append(root.val)
            DFS(root.left,s)
            DFS(root.right,s)
        
        DFS(root1,b1)
        DFS(root2,b2)

        return b1==b2