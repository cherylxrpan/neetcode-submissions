class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timemap.get(key, [])
        l = 0
        r = len(values) - 1
        while l<=r:
            m = (l+r)//2

            if values[m][1] <= timestamp:
                res  = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# i realize my biggest problem was with dictionary functions

        
