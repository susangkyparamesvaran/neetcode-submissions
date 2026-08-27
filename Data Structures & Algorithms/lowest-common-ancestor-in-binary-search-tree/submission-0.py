# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root

        while True:
            # this is if p and q are ancestors of eachother
            if p.val == lca.val or q.val == lca.val:
                return lca
            
            # if we are traversing to the left of the current lca
            if p.val < lca.val and q.val < lca.val:
                lca = lca.left

            # if we are traversing to the right of the current lca

            if p.val > lca.val and q.val > lca.val:
                lca = lca.right

            if p.val > lca.val and q.val < lca.val:
                return lca
            
            if q.val > lca.val and p.val < lca.val:
                return lca
            


