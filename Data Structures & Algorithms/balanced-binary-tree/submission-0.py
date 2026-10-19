# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def height(node):
            nonlocal balanced
            if not node:
                return 0
            L = height(node.left)
            R = height(node.right)
            if abs(L-R)>1:
                balanced = False
            return 1 + max(L, R)
        height(root)
        return balanced
                
