# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub_signature = self.serialise(subRoot)
        found = [False]
        
        def dfs(node):
            if not node:
                return '#'
            
            left = dfs(node.left)
            right = dfs(node.right)
            current = f"{node.val},{left},{right}"
            if current == sub_signature:
                found[0] = True
            return current
        
        dfs(root)
        return found[0]
  


    def serialise(self, node):
        if not node:
            return "#"
        left = self.serialise(node.left)
        right = self.serialise(node.right)
        return f"{node.val},{left},{right}"
