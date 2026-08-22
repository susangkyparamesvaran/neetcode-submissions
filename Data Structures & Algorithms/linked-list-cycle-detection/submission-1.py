# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # notes:
        # Each node can only point to at most one node
        # we can use a hash table, to see what nodes have been seen, and if node.next 
        # is in the hash table then we return true

        current = head
        seen = {}

        while (current):
            if (current not in seen):
                seen[current] = True
            else:
                return True

            current = current.next
        
        return False
        



        