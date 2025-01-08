class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = left = ListNode(0)
        right_head = right = ListNode(0)
        
        current = head
        while current:
            if current.val < x:
                left.next = current  
                left = left.next
            else:
                right.next = current  
                right = right.next
            current = current.next
        
        left.next = right_head.next
        right.next = None
        
        return left_head.next
