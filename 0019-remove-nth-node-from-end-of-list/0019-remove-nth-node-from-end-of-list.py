# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        dummy = ListNode()
        dummy.next = head
        pointer1 = dummy
        pointer2 = dummy 

        for i in range(n):
            pointer2 = pointer2.next
        
        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        pointer1.next = pointer1.next.next


        return dummy.next
        
        
        