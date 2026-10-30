class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        
        for course, pre in prerequisites:
            indegree[pre] += 1
            adj[course].append(pre)

        res = []
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        while q:
            node = q.popleft()
            res.append(node)
            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return res[::-1] if len(res) == numCourses else []