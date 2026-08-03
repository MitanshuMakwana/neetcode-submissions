# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while (l1 is not None) or (l2 is not None) or (carry != 0):
            ans = carry

            if l1 is not None:
                ans += l1.val
                l1 = l1.next
            if l2 is not None:
                ans += l2.val
                l2 = l2.next
            
            carry = ans//10
            curr.next = ListNode(ans % 10)
            curr = curr.next
        return dummy.next