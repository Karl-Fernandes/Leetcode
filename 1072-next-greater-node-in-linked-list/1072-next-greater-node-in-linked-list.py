# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current = head
        stack = []
        hashMap = {}
        answer = []
        
        while current:
            while stack and stack[-1].val < current.val:
                hashMap[stack.pop()] = current.val
            stack.append(current)
            current = current.next
        
        pointer2 = head
        while pointer2:
            if pointer2 in hashMap:
                answer.append(hashMap[pointer2])
            else:
                answer.append(0)
            pointer2 = pointer2.next

        return answer


        
        
                


        