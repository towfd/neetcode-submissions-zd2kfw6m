class TimeMap:
    # Approach: HashMap of sorted (timestamp, value) lists + Binary Search
    # Since set() is always called with strictly increasing timestamps,
    # each key's list is naturally sorted by timestamp — no explicit sorting needed.
    #
    # set(): append (timestamp, value) to the list for the given key. O(1).
    #
    # get(): binary search the key's list for the largest timestamp <= the query timestamp.
    #   - If an exact match is found, return its value immediately.
    #   - If the query timestamp is larger than mid's timestamp, move left pointer right
    #     (there might be a closer match to the right).
    #   - If smaller, move right pointer left.
    #   - When the loop exits, r_idx points to the largest timestamp that did not exceed
    #     the query. If r_idx >= 0, that entry is the answer; otherwise return "".
    # Time Complexity: set O(1), get O(log N) where N = number of entries for the key.
    # Space Complexity: O(total number of set calls).
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
