# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pointer1 = head
        pointer2 = pointer1.next

        while pointer1 and pointer2:
            pointer1.val, pointer2.val = pointer2.val, pointer1.val

            pointer1 = pointer2.next
            pointer2 = pointer1.next if pointer1 and pointer1.next else None
        
        return head
        