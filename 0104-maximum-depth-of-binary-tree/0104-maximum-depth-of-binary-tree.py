# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        return max(left, right) 
        
        
    
    def traverse(self, root):
        if not root:
            return 1
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        return max(left, right) + 1
        