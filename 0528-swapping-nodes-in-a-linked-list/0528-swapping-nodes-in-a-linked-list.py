class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = r = head
        for _ in range(k-1):
            l = l.next
        
        tail = l
        while tail.next:
            tail, r = tail.next, r.next
        
        l.val, r.val = r.val, l.val
        return head
        
