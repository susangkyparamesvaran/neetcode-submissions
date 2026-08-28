# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_val = root.val
        queue = [(root, max_val)]
        good = 0

        while (queue):
            # pop head
            # contains the max of the parents of node
            node, current_max = queue.pop(0)

            # if the val has a better parents of node
            if current_max <= node.val:
                current_max = node.val
                good = good + 1
            
            if (node.left):
                queue.append((node.left, current_max))
            
            if (node.right):
                queue.append((node.right, current_max))
        
        return good
            



