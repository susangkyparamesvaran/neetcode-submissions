# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # assume tree is balanced
        balanced = True

        def dfs_check(node):

            nonlocal balanced

            if not node:
                return 0

            left_depth = dfs_check(node.left)
            right_depth = dfs_check(node.right)

            if (abs(left_depth - right_depth) > 1):
                balanced = False

            return (max(left_depth, right_depth) + 1)
        
        dfs_check(root)

        return balanced