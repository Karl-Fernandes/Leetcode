class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(node):
            if not node or not self.balanced:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                self.balanced = False
            
            return max(left, right) + 1

        dfs(root)
        return self.balanced
