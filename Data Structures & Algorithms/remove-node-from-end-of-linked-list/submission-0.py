# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head
        
        i = 0
        while (right):
            i = i + 1
            right = right.next
        
        iterate = i - n

        j = 0
        while (j < iterate):
            j = j + 1
            left = left.next
        
        left.next = left.next.next

        return dummy.next

            

        

