# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pointer1 = dummy
        pointer2 = dummy
        
        for i in range(n):
            pointer1 = pointer1.next

        while pointer1.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        pointer2.next = pointer2.next.next

        return dummy.next

        

        
        

        