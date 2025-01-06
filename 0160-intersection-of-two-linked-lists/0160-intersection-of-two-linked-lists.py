# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer1 = headA
        nodes = set()

        while pointer1:
            nodes.add(pointer1)
            pointer1 = pointer1.next
            
        pointer2 = headB
        while pointer2:
            if pointer2 in nodes:
                return pointer2
            nodes.add(pointer2)
            pointer2 = pointer2.next

        return None
        