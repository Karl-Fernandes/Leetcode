# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: idx for idx, val in enumerate(inorder)}

        # Use an index pointer for preorder
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None
            
            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1

            index = inorder_index[root.val]

            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)

            return root
        
        return helper(0, len(inorder) - 1)

         
        