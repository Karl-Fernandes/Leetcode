# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Blue Hat
# This seems like a travel question, we need to check whether both trees are equal

# Yellow hat
# We can traverse trees using bfs or dfs

# Black hat
# One of the trees might not even exist so we can check that firstly

# Red hat
# I think this problem should be visually easier to undersstand

# Green hat
# Why should I use dfs? DFS would allow me to recurse to the bottom of each branch, we can use dfs and traverse the same thing on both trees
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
        