# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isSame(self,p,q):
        if(p==None and q==None):
            return True
        if(p==None or q==None or p.val!=q.val):
            return False
        return self.isSame(p.right,q.right) and self.isSame(p.left,q.left)

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        # flag= False
        # def dfs(root):
        #     if not root:
        #         return
        #     if root==subRoot:
        #         flag=True
        #         return
        #     if root.left:
        #         dfs(root.left)
        #     if root.right:
        #         dfs(root.right)
        #     # if not root.left and not root.right:
        #     #     return 
        # if(root == None and subRoot == None) : return True
        # if(root == None or subRoot == None) : return False
        # return (subRoot == root) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        # return flag
        if(root==None):
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        