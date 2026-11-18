class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(dict)
        for w in words:
            for c in w:
                adj[c] = set()
        indegrees = {c: 0 for c in adj}

        for w1, w2 in zip(words, words[1:]):      # adjacent pairs
            for a, b in zip(w1, w2):
                if a != b:
                    adj[a].add(b)               # a comes before b
                    break         
            else:                
                if len(w1) > len(w2):
                    return ""               
        
        for a in adj:
            for b in adj[a]:
                indegrees[b] += 1

        q = deque([c for c in indegrees if indegrees[c] == 0])
        order = []

        while q:
            c = q.popleft()
            order.append(c)
            for neighbor in adj[c]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)

        if len(order) != len(indegrees):
            return ""

        return "".join(order)