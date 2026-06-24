class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 暴力破解
        # 跑兩個迴圈 第一個迴圈會建立一個hashtable, 紀錄目前陣列所有字符的頻率以及目前最大頻率
        # 第二個迴圈 從第一個迴圈的index開始跑，會去計算目前所有字符的頻率並更新最大頻率
        # 時間複雜度 O(N^2)
        # 空間複雜度 O(26) -> 字母數量
        max_len = 0
        for i in range(len(s)):
            h_table = {}
            max_freq = 0
            for j in range(i, len(s)):
                char = s[j]
                h_table[char] = h_table.get(char, 0) + 1

                max_freq = max(max_freq, h_table[char])
                current_len = j - i + 1
                if current_len - max_freq <= k:
                    max_len = max(max_len, current_len)
        return max_len