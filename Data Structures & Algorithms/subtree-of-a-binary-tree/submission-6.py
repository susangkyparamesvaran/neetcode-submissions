# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if subRoot is None:
            return True
        
        queue = [root]

        while (queue):
            node = queue.pop(0)

            if node is None:
                continue

            if (node.val == subRoot.val):
                queue1 = [node]
                queue2 = [subRoot]

                result = True

                # 2 queues containing these "roots"
                # dequeue the heads from the queues
                while (queue1 and queue2):
                    v1 = queue1.pop(0)
                    v2 = queue2.pop(0)

                    if (v1 is None and v2 is None):
                        continue
                    
                    if (v1 is None and v2 is not None):
                        result = False
                        break
                    
                    if (v1 is not None and v2 is None):
                        result = False
                        break
                    
                    if (v1.val != v2.val):
                        result = False
                        break
                    

                    # add children to queue
                    queue1.append(v1.left)
                    queue1.append(v1.right)
                    
                    queue2.append(v2.left)
                    queue2.append(v2.right)
                    
                if result and not queue1 and not queue2:
                    return True

            
            if node is None:
                continue
                
            if (node.left):
                queue.append(node.left)
                
            if (node.right):
                queue.append(node.right)
        
        return False


