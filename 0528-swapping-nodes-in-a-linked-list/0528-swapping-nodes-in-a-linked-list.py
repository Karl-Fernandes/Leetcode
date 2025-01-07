class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        array = []
        new_list = ListNode(0)
        current = new_list

        while head:
            array.append(head.val)
            head = head.next
        
        n = len(array)
        array[k - 1], array[n - k] = array[n - k], array[k - 1]
        
        for val in array:
            current.next = ListNode(val)
            current = current.next
        
        return new_list.next
