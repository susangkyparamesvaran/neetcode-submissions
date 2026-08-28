# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
            
        result = []

        curr_level = 1
        next_level = 0

        queue = [root]
        while (queue):
            i = 0
            j = 0

            level = []
            while (i < curr_level):
                node = queue.pop(0)
                level.append(node.val)
                
                if (node.left):
                    queue.append(node.left)
                    j = j + 1
                

                if (node.right):
                    queue.append(node.right)
                    j = j + 1

                i = i + 1
                
            next_level = j
            curr_level = next_level
            next_level = 0

            for i in range(len(level) - 1, -1, -1):
                if level[i] is None:
                    continue
                else:
                    value = level[i]
                    result.append(value)
                    break

        return result





