class TimeMap:
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((timestamp, value))
        else:
            self.time_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
            
        key_list = self.time_map[key]
        l_idx, r_idx = 0, len(key_list) - 1
        while l_idx <= r_idx:
            mid = (l_idx + r_idx) // 2
            if timestamp == key_list[mid][0]:
                return key_list[mid][1]
            elif timestamp > key_list[mid][0]:
                l_idx = mid + 1
            else:
                r_idx = mid - 1

        if r_idx >= 0:
            return key_list[r_idx][1]
        return ""
