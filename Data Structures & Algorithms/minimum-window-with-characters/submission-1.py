class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 建立一個len 128的list, 因為標準ascii字母總共128字元
        # 使用ord(char)將字母轉成數字的index, 加1
        # 過濾掉s裡面不需要的字母，留下有用的字母，並記錄他們原本index的位子
        # 使用雙指標去跑，右指標會去計算目前sliding window內的字母是否跟t的陣列相符合
        # 待右指標跑到完全相同的陣列並計算最小長度後，左指標開始往右跑，直到陣列不符合為止，後循環到右指標跑到最後一個字母
        # 後續看最小長度有無被更改，有被更改代表有被變更過，回傳最小長度，沒更改回傳 ""
        # 時間複雜度 O(N)
        # 空間複雜度 O(M) -> ASCII陣列的空間
        t_list = [0] * 128
        required_types = 0

        for char in t:
            if t_list[ord(char)] == 0:
                required_types += 1
            t_list[ord(char)] += 1

        filtered_s = []
        for i, char in enumerate(s):
            if t_list[ord(char)] > 0:
                filtered_s.append((i, char))

        window_count = [0] * 128
        archieve = 0
        min_len = float('inf')
        best_start, best_end = 0, 0
        lindex = 0

        for rindex in range(len(filtered_s)):
            r_idx, r_char = filtered_s[rindex]
            r_ascii = ord(r_char)
            window_count[r_ascii] += 1
            if window_count[r_ascii] == t_list[r_ascii]:
                archieve += 1

            while archieve == required_types:
                l_idx, l_char = filtered_s[lindex]
                l_ascii = ord(l_char)
                current_len = r_idx - l_idx + 1
                if min_len > current_len:
                    min_len = current_len
                    best_start, best_end = l_idx, r_idx

                window_count[l_ascii] -= 1
                if window_count[l_ascii] < t_list[l_ascii]:
                    archieve -= 1
                lindex += 1

        if min_len == float('inf'):
            return ""
        else:
            return s[best_start: best_end + 1]