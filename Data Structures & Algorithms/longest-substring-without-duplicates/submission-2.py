class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 暴力破解
        # 複製一份s出來
        # 寫個while迴圈，條件為當ss為空時結束
        # 將輸入過的字元放入set中，每次檢查是否有在set內了
        # 檢查到後計算當前set內數量，接著遍歷所有的字串
        # 回傳最大值
        # 時間複雜度O(n^2)
        # 空間複雜度O(n)
        max_len = 0
        i = 0
        ss = s
        
        while len(ss) != 0:
            st = set()
            for n in ss:
                if n not in st:
                    st.add(n)
                else:
                    break
                if len(st) > max_len:
                    max_len = len(st)
                    
            i += 1           
            ss = s[i:]
        return max_len
