class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # 建立兩個指針，以及一個hash_table用來記錄出現頻率
        # 當目前長度 - 最大出現頻率不夠k時，將左指針往後移動，並且扣除hash_table內相關的頻率
        # 回傳最大的值
        # 時間複雜度 O(n)
        # 空間複雜度 O(26) -> 字母數量
        lindex = 0
        max_len = 0
        max_freq = 0
        freq_table = {}
        for rindex in range(len(s)):
            char = s[rindex]
            freq_table[char] = freq_table.get(char, 0) + 1
            max_freq = max(max_freq, freq_table[char])
            while (rindex - lindex + 1) - max_freq > k:
                freq_table[s[lindex]] -= 1
                lindex += 1
            max_len = max(max_len, rindex - lindex + 1)
        return max_len