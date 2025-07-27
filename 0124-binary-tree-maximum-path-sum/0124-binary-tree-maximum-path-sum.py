# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float('-inf')]


        def dfs(current):
            if not current:
                return 0
            
            left = max(0, dfs(current.left))
            right = max(0, dfs(current.right))

            max_sum[0] = max(max_sum[0], current.val + left + right)

            return current.val + max(left, right)      

        dfs(root)

        return max_sum[0]
        