class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        # 建立兩個指針，一個指針先往前跑，邊跑邊將字母輸入進set內，並計數
        # 若右指針遇到重複的字母，左指針開始跑，跑到吐掉重複的字母為止，持續到全部的字母跑完
        # 回傳最大計數
        # 時間複雜度 O(n)
        # 空間複雜度 O(n)

        lindex = 0
        sset = set()
        max_len = 0
        
        for rindex in range(len(s)):            
            while s[rindex] in sset:
                sset.remove(s[lindex])
                lindex += 1                
            sset.add(s[rindex])            
            max_len = max(max_len, len(sset))
            
        return max_len