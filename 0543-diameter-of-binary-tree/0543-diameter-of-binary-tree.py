# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0  # shared state across all calls

        def dfs(node):
            if not node:
                return 0  # base case: height is 0
            
            left = dfs(node.left)     # height of left subtree
            right = dfs(node.right)   # height of right subtree

            # diameter at this node is left + right
            self.maxDiameter = max(self.maxDiameter, left + right)

            return max(left, right) + 1  # height of current subtree

        dfs(root)
        return self.maxDiameter
