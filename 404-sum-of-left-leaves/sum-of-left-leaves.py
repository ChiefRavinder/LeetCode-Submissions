class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:  # Leaf node
                if is_left:
                    return node.val
                else:
                    return 0
            left_sum = dfs(node.left, True)   # Traverse left child
            right_sum = dfs(node.right, False)  # Traverse right child
            return left_sum + right_sum
        
        return dfs(root, False)
              