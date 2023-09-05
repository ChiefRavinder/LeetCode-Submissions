# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
        

#         def dfs(node,minn,maxx):
#             if not node:
#                 return 
#             pivot=node.val
#             if node.left:
#                 if node.left.val>=minn and node.left.val>=pivot:
#                     return False
#                 else:
#                     minn==node.left.val
#             if node.right:
#                 if node.right.val<=maxx and node.left.val<=pivot:
#                     return False
#                 else:
#                     maxx=node.right.val
            

#             dfs(node.left,pivot,maxx)
#             dfs(node.right,minn,pivot)

#             return True

        # return dfs(root,(float('inf')),(float('-inf')))

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # Helper function to check if a binary tree is a valid BST
        def is_valid_bst(node, min_val, max_val):
            if not node:
                return True
            
            # Check if the current node's value is within the valid range
            if min_val is not None and node.val <= min_val:
                return False
            if max_val is not None and node.val >= max_val:
                return False
            
            # Recursively check the left and right subtrees with updated range
            return (is_valid_bst(node.left, min_val, node.val) and
                    is_valid_bst(node.right, node.val, max_val))
        
        # Start the validation with an initial range of None for both min and max values
        return is_valid_bst(root, None, None)

        
        