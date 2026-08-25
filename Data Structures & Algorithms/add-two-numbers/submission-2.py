# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # this is where we will store the result
        dummy = node = ListNode(0)
        carry = 0

        while (l1 or l2):
            
            val1 = l1.val if (l1) else 0
            val2 = l2.val if (l2) else 0

            sum = val1 + val2 + carry
            
            if (sum < 10):
                value = sum
                carry = 0
            else:
                carry = sum // 10
                value = sum % 10
            
            node.next = ListNode(value)
            node = node.next
            
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        if (carry != 0):
            node.next = ListNode(carry)

        return dummy.next