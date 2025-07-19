class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Ensure p is always the smaller value - compare by .val
        if p.val > q.val:
            p, q = q, p
        
        def dfs(node):
            if not node:
                return None
            
            if node.val > q.val:
                return dfs(node.left)
            elif node.val < p.val:
                return dfs(node.right)
            else:
                return node
        
        return dfs(root)