class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        answer = [0] * len(values)
        stack = []
        
        for i, val in enumerate(values):
            while stack and values[stack[-1]] < val:
                answer[stack.pop()] = val
            stack.append(i)
        
        return answer
