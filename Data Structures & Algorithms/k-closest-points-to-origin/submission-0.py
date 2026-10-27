class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heap.append((x * x + y * y, x, y))   # (squared distance, point)
        heapq.heapify(heap)                      # closest at the top

        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)     # take the closest remaining
            res.append([x, y])
        return res