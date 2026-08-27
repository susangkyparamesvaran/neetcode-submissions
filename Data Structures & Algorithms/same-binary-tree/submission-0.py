# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # define 2 queues for p and q

        p_queue = [p]
        q_queue = [q]

        while (p_queue and q_queue):

            # delete heads from queues
            pv = p_queue.pop(0)
            qv = q_queue.pop(0)

            if (pv is None and qv is None):
                continue
            elif (pv is None and qv is not None):
                return False
            elif (qv is None and pv is not None):
                return False
            elif (pv.val != qv.val):
                return False
        
            # add p children
            if (pv.left):
                p_queue.append(pv.left)
            else:
                p_queue.append(None)
            if (pv.right):
                p_queue.append(pv.right)
            else:
                p_queue.append(None)

            # add q children
            if (qv.left):
                q_queue.append(qv.left)
            else:
                q_queue.append(None)
            if (qv.right):
                q_queue.append(qv.right)
            else:
                q_queue.append(None)
            
            
        if (p_queue) or (q_queue):
            return False
        
        return True
            
            

