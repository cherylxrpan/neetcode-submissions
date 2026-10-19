# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            out = []
            def dfs(node):
                if not node:
                    out.append(",#")
                    return
                out.append("," + str(node.val))
                dfs(node.left)
                dfs(node.right)
            dfs(node)
            return "".join(out)
        
        return serialize(subRoot) in serialize(root)
        