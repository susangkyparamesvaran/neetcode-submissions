# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    
        if not root:
            return 0
        
        # max depth of left subtree
        left = self.maxDepth(root.left)
        # max depth of right subtree
        right = self.maxDepth(root.right)

        value = max(left,right) + 1

        return value



