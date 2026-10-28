"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        graph = {}
        graph[node] = Node(node.val)
        q = deque([node])
        while q:
            cur = q.popleft()
            # wire neighbors to the node
            for n in cur.neighbors:
                if n not in graph:
                    graph[n] = Node(n.val)
                    q.append(n)
                graph[cur].neighbors.append(graph[n])

        return graph[node]