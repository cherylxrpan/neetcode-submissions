# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        # Job 1: BFS over every node in root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if self.isSame(node, subRoot):     # Job 2: check this starting point
                return True                    # found a match, done
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False                           # tried every node, no match

    def isSame(self, p, q):                    # your Same Tree code, unchanged
        queue = deque([(p, q)])
        while queue:
            a, b = queue.popleft()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False                   # only ends THIS check
            queue.append((a.left, b.left))
            queue.append((a.right, b.right))
        return True