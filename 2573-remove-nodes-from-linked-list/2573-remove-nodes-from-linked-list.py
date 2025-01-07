# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        stack = []

        while pointer:
            while stack and stack[-1].val < pointer.val:
                stack.pop()
            
            stack.append(pointer)
            pointer = pointer.next
            
        for i in range(len(stack) - 1):
                    stack[i].next = stack[i + 1]
        
        if stack:
            stack[-1].next = None
        
        return stack[0] if stack else None
        

        