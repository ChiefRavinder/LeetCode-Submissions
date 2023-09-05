# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# queue=[]  nextQ=[] level=[] res=[]

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=[root]
        nextQ=[]
        res=[]
        level=[]
        while q:
            
            for root in q:
                if root:
                    level.append(root.val)
                    if root.left:
                        nextQ.append(root.left)
                    if root.right:
                        nextQ.append(root.right)
            res.append(level)
            q=nextQ
            level=[]
            nextQ=[]
        return res




        
        
        