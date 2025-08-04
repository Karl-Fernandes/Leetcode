class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in mapping:  # opening bracket
                stack.append(char)
            else:  # closing bracket
                if not stack or mapping[stack.pop()] != char:
                    return False
        
        return not stack  
