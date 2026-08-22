# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # notes:
        # Each node can only point to at most one node
        # we can't use the same approach of looping through until None
        # since this could lead to an infinite loop if there is a cycle
        # we can use a hash table, to see what nodes have been seen, and if node.next 
        # is in the hash table then we return the index

        # if index == -1, then return False, else return True

        current = head
        i = 0
        seen = {}

        while (current):
            if (current not in seen):
                seen[current] = i
            else:
                return True

            current = current.next
            i = i + 1
        
        return False
        



        