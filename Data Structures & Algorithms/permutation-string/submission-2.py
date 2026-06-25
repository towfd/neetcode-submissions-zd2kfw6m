class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding windows
        # 創建兩個指標 這次sliding window的長度會跟s1一模一樣
        # 創建兩個hashmap, 裡面放目前s1以及目前窗口的字母
        # 若壹模壹樣就回傳True，若到結束都還沒有找到 回傳False
        # 時間複雜度O(N)
        # 空間複雜度O(N)
        if len(s1) > len(s2):
            return False

        s1_hashmap = {}
        s2_hashmap = {}
        for s in s1:
            s1_hashmap[s] = s1_hashmap.get(s, 0) + 1

        for s in s2[:len(s1)]:
            s2_hashmap[s] = s2_hashmap.get(s, 0) + 1

        if s1_hashmap == s2_hashmap:
            return True

        for rindex in range(len(s1), len(s2)):
            s2_hashmap[s2[rindex]] = s2_hashmap.get(s2[rindex], 0) + 1
            
            s2_hashmap[s2[rindex - len(s1)]] = s2_hashmap.get(s2[rindex - len(s1)], 0) - 1
            if s2_hashmap[s2[rindex - len(s1)]] == 0: del s2_hashmap[s2[rindex - len(s1)]]
            if s1_hashmap == s2_hashmap:
                return True
        return False
