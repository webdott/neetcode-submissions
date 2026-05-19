class TimeMap:

    def __init__(self):
        self.map_ = defaultdict(list)

    def closest_timestamp_val(self, values: list[int], timestamp: int) -> str:
        l, r = 0, len(values) - 1

        while l < r:
            m = (l + r) // 2

            if values[m][0] > timestamp:
                r = m
            else:
                l = m + 1

        ts, val = values[l]

        if ts <= timestamp:
            return val
        elif l > 0:
            return values[l-1][1]
        else:
            return ""

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map_[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map_:
            return self.closest_timestamp_val(self.map_[key], timestamp)

        return ""
