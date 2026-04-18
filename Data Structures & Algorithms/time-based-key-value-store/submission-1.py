from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.tmap:
            idx = bisect_right(self.tmap[key], timestamp, key=lambda x: x[0])
            return self.tmap[key][idx - 1][1] if idx > 0 else ""
        return ""