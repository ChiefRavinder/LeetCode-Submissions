# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        
        def inorder(root,lis):
            
            if root!=None:
                inorder(root.left,lis)
                lis.append(root.val)
                inorder(root.right,lis)
            return lis
        return inorder(root,[])

# class Solution(object):
#     def inorderTraversal(self, root):
        
#         def inorder(root, lis):
#             if root is not None:
#                 inorder(root.left, lis)
#                 lis.append(root.val)
#                 inorder(root.right, lis)
#             return lis
        
#         return inorder(root, [])