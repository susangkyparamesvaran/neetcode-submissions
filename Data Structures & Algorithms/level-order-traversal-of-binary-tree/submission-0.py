# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]

        level = []
        result = []

        curr_level = 1
        next_level = 0

        while (queue):
            # for each level
            i = 0
            j = 0
            level = []

            while i < curr_level:
                node = queue.pop(0)
                level.append(node.val)

                if (node.left):
                    queue.append(node.left)
                    j = j + 1
                
                if (node.right):
                    queue.append(node.right)
                    j = j + 1
                
                i = i + 1
            
            result.append(level)
            
            next_level = j
            curr_level = next_level
            next_level = 0

        return result