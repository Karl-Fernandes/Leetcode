class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {']': '[', '}': '{', ')': '('}
        stack = []

        for char in s:
            if char in valid_pairs:  
                if not stack or stack.pop() != valid_pairs[char]:
                    return False
            else:  
                stack.append(char)
        
        return not stack