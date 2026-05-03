class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))
        print(self.timeMap)

    def get(self, key: str, timestamp: int) -> str:
        for i in range(len(self.timeMap[key]) - 1, -1, -1):
            if self.timeMap[key][i][1] <= timestamp:
                return self.timeMap[key][i][0]
        return ""