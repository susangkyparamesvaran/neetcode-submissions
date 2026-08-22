# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # So the order that the new linked list needs to be in is: beg end beg end
        # split list into 2
        
        slow = head
        fast = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        # slow contains the middle value right now, so anything to the right should
        # be added to the big list, and reversed
        
        # this is our head of the list for the new half
        second = slow.next
        # This is so that the previous list also points to None 1 ->2 ->3 -> None
        slow.next = None
        prev_node = None
        while (second):
            # save what the next node needs to be (what we need to iterate to)
            next_node = second.next
            # we change the next pointer so that it points the previous node
            second.next = prev_node
            # this becomes the new previous node
            prev_node = second
            # and we iterate to the next node
            second = next_node

        # prev_node will return the head
        first = head
        second = prev_node

        while (second):
            small = first.next
            big = second.next

            first.next = second
            second.next = small

            first = small
            second = big

                
